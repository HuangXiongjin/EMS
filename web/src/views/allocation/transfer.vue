<template>
  <el-row :gutter="15">
    <el-col :span="24">
      <el-form :inline="true">
        <el-row>
          <el-col :span="24">
            <el-form-item label="调拨单号">
              <el-input v-model="TableData.searchField.No" placeholder="请输入调拨单号" size="mini" style="width: 150px;"></el-input>
            </el-form-item>
            <el-form-item label="设备编号">
              <el-input v-model="TableData.searchField.EquipmentCode" placeholder="请输入设备编号" size="mini" style="width: 150px;"></el-input>
            </el-form-item>
            <el-form-item label="设备名称">
              <el-input v-model="TableData.searchField.EquipmentName" placeholder="请输入设备名称" size="mini" style="width: 150px;"></el-input>
            </el-form-item>
            <el-form-item>
              <el-button type="primary" size="mini" @click="getTableData">查询</el-button>
            </el-form-item>
          </el-col>
        </el-row>
      </el-form>
      <div class="platformContainer">
        <el-table :data="TableData.data" border size="mini" :header-cell-style="{ 'background':'#F5F7FA' }" ref="multipleTable">
          <el-table-column prop="No" label="调拨单号">
            <template slot-scope="scope">
              <a href="javascript:;" style="color:#2196F3;" @click="seeDetails(scope.row)">{{ scope.row.No }}</a>
            </template>
          </el-table-column>
          <el-table-column prop="EquipmentName" label="设备名称"></el-table-column>
          <el-table-column prop="EquipmentCode" label="设备编号"></el-table-column>
          <el-table-column prop="Specs" label="规格型号"></el-table-column>
          <el-table-column prop="AllocationDepartment" label="调拨部门"></el-table-column>
          <el-table-column prop="AddressOut" label="调出地点"></el-table-column>
          <el-table-column prop="AddressInto" label="调入地点"></el-table-column>
          <el-table-column prop="Comment" label="调拨原因"></el-table-column>
          <el-table-column prop="Time" label="申请时间"></el-table-column>
          <el-table-column prop="User" label="申请人"></el-table-column>
          <el-table-column prop="Node" label="当前节点"></el-table-column>
          <el-table-column prop="Status" label="审批状态">
            <template slot-scope="scope">
              <div v-for="(item,index) in TableData.ProcessStructure.nodes" :key="index">
                <span class="btn-block color-white" v-if="item.state === scope.row.Status" :style="{ background:item.stateColor }">{{ scope.row.Status }}</span>
              </div>
            </template>
          </el-table-column>
        </el-table>
        <div class="paginationClass">
          <el-pagination background  layout="total, sizes, prev, pager, next, jumper"
           :total="TableData.total"
           :current-page="TableData.offset"
           :page-sizes="[10,20,30,40,50]"
           :page-size="TableData.limit"
           @size-change="handleSizeChange"
           @current-change="handleCurrentChange">
          </el-pagination>
        </div>
        <el-dialog title="调拨单" :visible.sync="TableData.detailsDialogVisible" width="60%" :append-to-body="true">
          <el-form :inline="true">
            <el-form-item v-for="(item,index) in TableData.handleBtns" :key="index">
              <el-button type="primary" size="mini" @click="approval(item)">{{ item.label }}</el-button>
            </el-form-item>
          </el-form>
          <p class="marginBottom">基本信息</p>
          <table class="elementTable text-size-14 marginBottom">
            <tr>
              <td>设备名称</td>
              <td>{{ TableData.detailsInfo.EquipmentName }}</td>
              <td>设备编号</td>
              <td>{{ TableData.detailsInfo.EquipmentCode }}</td>
              <td>规格型号</td>
              <td>{{ TableData.detailsInfo.Specs }}</td>
            </tr>
            <tr>
              <td>调拨部门</td>
              <td>{{ TableData.detailsInfo.AllocationDepartment }}</td>
              <td>调出地点</td>
              <td>{{ TableData.detailsInfo.AddressOut }}</td>
              <td>调入地点</td>
              <td>{{ TableData.detailsInfo.AddressInto }}</td>
            </tr>
            <tr>
              <td>调拨原因</td>
              <td>{{ TableData.detailsInfo.Comment }}</td>
              <td>申请时间</td>
              <td>{{ TableData.detailsInfo.Time }}</td>
              <td>申请人</td>
              <td>{{ TableData.detailsInfo.User }}</td>
            </tr>
            <tr>
              <td>当前节点</td>
              <td>{{ TableData.detailsInfo.Node }}</td>
              <td>审批状态</td>
              <td colspan="3">
                <div v-for="(item,index) in TableData.ProcessStructure.nodes" :key="index">
                  <span class="btn-block color-white" v-if="item.state === TableData.detailsInfo.Status" :style="{ background:item.stateColor }">{{ TableData.detailsInfo.Status }}</span>
                </div>
              </td>
            </tr>
          </table>
          <p class="marginBottom">审批信息</p>
          <el-table class="marginBottom" :data="TableData.LifeTableData" border size="mini" :header-cell-style="{ 'background':'#F5F7FA' }">
            <el-table-column prop="No" label="单号"></el-table-column>
            <el-table-column prop="Time" label="操作时间"></el-table-column>
            <el-table-column prop="User" label="操作人"></el-table-column>
            <el-table-column prop="Node" label="当前节点"></el-table-column>
            <el-table-column prop="Status" label="当前状态"></el-table-column>
            <el-table-column prop="Content" label="操作内容"></el-table-column>
          </el-table>
          <p class="marginBottom">审批流程</p>
          <div id="container" style="position:relative;width: 100%;height: 300px;"></div>
          <span slot="footer" class="dialog-footer">
            <el-button @click="TableData.detailsDialogVisible = false">取 消</el-button>
          </span>
        </el-dialog>
      </div>
    </el-col>
  </el-row>
</template>

<script>
  import G6 from '@antv/g6';
  var moment = require('moment');
  export default {
    name: "transfer",
    data(){
      return{
        TableData:{
          tableName:"Allocation",
          workflow:"调拨转移",
          ProcessStructure:"",
          data:[],
          limit: 10,
          offset: 1,
          total: 0,
          searchField:{
            No:"",
            EquipmentCode:"",
            EquipmentName:"",
          },
          fieldModel:{
            ID:"",
            No:"",
            EquipmentCode:"",
            EquipmentName:"",
          },
          detailsDialogVisible:false,
          detailsInfo:{},
          handleBtns:[],
          LifeTableData:[]
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
