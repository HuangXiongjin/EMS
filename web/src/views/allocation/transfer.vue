<template>
  <FlowInstance :enableData="transferData"></FlowInstance>
</template>

<script>
  var moment = require('moment');
  import FlowInstance from "../../components/FlowInstance.vue"
  export default {
    name: "transfer",
    components:{ FlowInstance },
    data(){
      return{
        transferData:{
          workflowID:"3",
          tableName:"Allocation",
          tableColumn:[
            {label:"计划单号",prop:"No"},
            {label:"流程ID",prop:"TID"},
            {label:"设备编号",prop:"EquipmentCode"},
            {label:"设备名称",prop:"KeepEquipment"},
            {label:"调拨部门",prop:"AllocationDepartment"},
            {label:"调出地点",prop:"AddressOut"},
            {label:"调入地点",prop:"AddressInto"},
            {label:"调拨原因",prop:"Comment"},
            {label:"申请人",prop:"User"},
            {label:"创建时间",prop:"Time"},
            {label:"当前节点",prop:"Node"},
            {label:"当前状态",prop:"Status"},
          ],
          FlowType:"", //默认为空代表不区分流程是计划还是任务 task任务 plan计划
          No:"No",
          EquipmentCode:"EquipmentCode",
          EquipmentName:"EquipmentName",
          Time:"FoundTime",
          User:"PlanUser",
          Node:"Node",
          Status:"Status",
        },
        graph:null,
      }
    },
    mounted(){
      this.getTableData()
      this.getWorkflow()
    },
    methods:{
      getTableData(){
        var that = this
        var params = {
          tableName: this.TableData.tableName,
          limit:this.TableData.limit,
          offset:this.TableData.offset - 1
        }
        for(var i in this.TableData.searchField){
          if(this.TableData.searchField[i]){
            params[i] = this.TableData.searchField[i]
          }
        }
        this.axios.get("/api/CUID",{
          params: params
        }).then(res => {
          if(res.data.code === "200"){
            that.TableData.data = res.data.data.rows
            that.TableData.total = res.data.data.total
          }else{
            that.$message({
              type: 'info',
              message: res.data.message
            });
          }
        })
      },
      handleSizeChange(limit){ //每页条数切换
        this.TableData.limit = limit
        this.getTableData()
      },
      handleCurrentChange(offset) { // 页码切换
        this.TableData.offset = offset
        this.getTableData()
      },
      //解析工作流 添加审批按钮
      getWorkflow(){
        var that = this
        var params = {
          tableName: "TechnologicalProcess",
          ProcessName:this.TableData.workflow,
        }
        this.axios.get("/api/CUID",{
          params: params
        }).then(res => {
          if(res.data.code === "200"){
            this.TableData.ProcessStructure = JSON.parse(res.data.data.rows[0].ProcessStructure)
          }else{
            that.$message({
              type: 'info',
              message: res.data.message
            });
          }
        })
      },
      seeDetails(row){
        this.TableData.detailsDialogVisible = true
        this.TableData.detailsInfo = row
        this.getBtn()
        this.getLife()
        this.init()
      },
      getBtn(){
        var nodeId = "" //当前节点的id
        var targetIdList = [] //目标节点Id列表
        this.TableData.ProcessStructure.nodes.forEach(item =>{ //解析工作流 获取当前节点的id
          if(item.label === this.TableData.detailsInfo.Node){
            nodeId = item.id
            this.TableData.ProcessStructure.edges.forEach(item =>{ //获取当前节点的目标节点
              if(item.source === nodeId){
                targetIdList.push(item.target)
              }
            })
          }
        })
        this.TableData.handleBtns = []
        //获取所有目标节点
        this.TableData.ProcessStructure.nodes.forEach(item =>{
          targetIdList.forEach(j =>{
            if(item.id === j){
              if(item.type != "triangle"){
                this.TableData.handleBtns.push(item)
              }
            }
          })
        })
        //判断目标节点是否有驳回子节点，有的话就渲染成按钮
        this.TableData.ProcessStructure.edges.forEach(item =>{
          targetIdList.forEach(j =>{
            if(item.source === j){ //获取目标节点的目标节点Id
              this.TableData.ProcessStructure.nodes.forEach(b =>{
                if(b.id === item.target){
                  if(b.type === "triangle"){
                    this.TableData.handleBtns.push(b)
                  }
                }
              })
            }
          })
        })
      },
      getLife(){
        var that = this
        var params = {
          tableName:"Life",
          No:this.TableData.detailsInfo.No,
        }
        this.axios.get("/api/CUID",{
          params: params
        }).then(res => {
          if(res.data.code === "200"){
            this.TableData.LifeTableData = res.data.data.rows
          }else{
            that.$message({
              type: 'info',
              message: res.data.message
            });
          }
        })
      },
      //审批按钮操作
      approval(row){
        let that = this
        var Status = ""
        var node = ""
        this.TableData.ProcessStructure.nodes.forEach(item =>{
          if(row.type === "triangle"){
            if(row.RefuseNode){
              if(item.id === row.RefuseNodeId){
                Status = item.state
                node = item.label
              }
            }
          }else{
            if(item.label === row.label){
              Status = item.state
              node = item.label
            }
          }
        })
        this.$confirm('您确定要进行'+ row.label +'操作吗？', '提示', {
          distinguishCancelAndClose:true,
          type: 'warning'
        }).then(()  => {
          var params = {
            tableName:that.TableData.tableName,
            ID:that.TableData.detailsInfo.ID,
            Status:Status,
            Node:node,
          }
          this.axios.put("/api/CUID",this.qs.stringify(params)).then(res =>{
            if(res.data.code === "200"){
              this.$message({
                type: 'success',
                message: res.data.message
              });
            }
            this.TableData.detailsDialogVisible = false
            this.getTableData()
            this.createLife(Status,row.label)
          },res =>{
            console.log("请求错误")
          })
        }).catch(() => {
          this.$message({
            type: 'info',
            message: '已取消操作'
          });
        });
      },
      //添加审批记录
      createLife(Status,label){
        var params = {
          tableName:"Life",
          No:this.TableData.detailsInfo.No,
          Time:moment().format("YYYY-MM-DD HH:ss:mm"),
          User:this.$store.state.UserName,
          Node:label,
          Status:Status,
          Content:label,
        }
        this.axios.post("/api/CUID",this.qs.stringify(params)).then(res =>{
          if(res.data.code === "200"){
            this.$message({
              type: 'success',
              message: "审批记录添加成功"
            });
          }else{
            this.$message({
              type: 'info',
              message: res.data.message
            });
          }
        },res =>{
          console.log("请求错误")
        })
      },
      init(){
        let that = this
        if(that.graph){
          that.graph.destroy()
        }
        this.$nextTick(() => {
          //虚线动画
          G6.registerEdge('circle-running',{
            afterDraw(cfg, group) {
              // get the first shape in the group, it is the edge's path here=
              const shape = group.get('children')[0];
              // the start position of the edge's path
              const startPoint = shape.getPoint(0);
              // add red circle shape
              const circle = group.addShape('circle', {
                attrs: {
                  x: startPoint.x,
                  y: startPoint.y,
                  fill: '#1890ff',
                  r: 3,
                },
                name: 'circle-shape',
              });
              // animation for the red circle
              circle.animate(
                ratio => {
                  // the operations in each frame. Ratio ranges from 0 to 1 indicating the prograss of the animation. Returns the modified configurations
                  // get the position on the edge according to the ratio
                  const tmpPoint = shape.getPoint(ratio);
                  // returns the modified configurations here, x and y here
                  return {
                    x: tmpPoint.x,
                    y: tmpPoint.y,
                  };
                },
                {
                  repeat: true, // Whether executes the animation repeatly
                  duration: 3000, // the duration for executing once
                },
              );
            },
          },'line');
          const width = document.getElementById('container').scrollWidth;
          const height = document.getElementById('container').scrollHeight;
          that.toolbar = new G6.ToolBar()
          that.graph = new G6.Graph({
            container: 'container',
            width,
            height,
            linkCenter: true,
            plugins: [that.toolbar],
            enabledStack: true, //是否启用redo & undo 栈功能，可进行撤销和回退
            modes: {
              default: [
                'drag-canvas',
                'zoom-canvas',
              ],
            },
            fitView: true,
          });
          //定义当前节点高亮
          that.TableData.ProcessStructure.nodes.forEach(item =>{ //解析工作流 获取当前节点的id
            if(item.label === that.TableData.detailsInfo.Node){
              item.style.fill = "#e6a23c"
            }
          })

          that.graph.read(that.TableData.ProcessStructure);
        })
      },
    }
  }
</script>

<style scoped>

</style>
