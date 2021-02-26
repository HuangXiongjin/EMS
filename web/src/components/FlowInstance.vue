<template>
    <el-row :gutter="20">
        <el-col :span="24" v-if="!showSteps">
            <div class="cardContainerHead">选择计划单号</div>
            <div class="cardContainer">
                <el-table :data="tableData" border size="mini" :header-cell-style="{ 'background':'#F5F7FA' }" ref="multipleTable">
                  <el-table-column v-for="(item,index) in enableData.tableColumn" :prop="item.prop" :label="item.label">
                    <template slot-scope="scope">
                        <a v-if="item.prop === enableData.No" href="javascript:;" style="color:#2196F3;" @click="stepDetails(scope.row)">{{ scope.row[enableData.No] }}</a>
                        <div v-for="(item,index) in ProcessStructure.nodes" :key="index" v-else-if="item.prop === enableData.Status">
                            <span class="btn-block color-white" v-if="item.state === scope.row[enableData.Status]" :style="{ background:item.stateColor }">{{ scope.row[enableData.Status] }}</span>
                        </div>
                        <span v-else>{{ scope.row[item.prop] }}</span>
                    </template>
                  </el-table-column>
                </el-table>
            </div>
        </el-col>
        <el-col :span="24" v-if="showSteps">
            <el-button class="marginBottom" size="mini" @click="showSteps = false">返回计划表</el-button>
            <el-steps :active="active" align-center finish-status="success">
              <el-step v-for="(item,index) in stepsList" :title="item.title"></el-step>
            </el-steps>
            <div class="platformContainer marginTop">
                <el-col :span="6">
                    <p class="marginBottom">当前信息</p>
                    <table class="elementTable text-size-14">
                        <tr v-for="(item,index) in enableData.tableColumn" :key="index">
                            <td>{{ item.label }}</td>
                            <td v-for="(value,key,i) in NoRow" :key="i" v-if="key === item.prop">
                                <span>{{ value }}</span>
                            </td>
                        </tr>
                    </table>
                </el-col>
                <el-col :span="18">
                    <p class="marginBottom">审批信息</p>
                    <el-form :inline="true">
                        <el-form-item v-for="(item,index) in handleBtns" :key="index">
                          <el-button type="primary" size="mini" @click="approval(item)">{{ item.label }}</el-button>
                        </el-form-item>
                    </el-form>
                    <el-table class="marginBottom" :data="LifeTableData" border size="mini" :header-cell-style="{ 'background':'#F5F7FA' }">
                        <el-table-column prop="No" label="单号"></el-table-column>
                        <el-table-column prop="Time" label="操作时间" width="170"></el-table-column>
                        <el-table-column prop="User" label="操作人"></el-table-column>
                        <el-table-column prop="Node" label="当前节点"></el-table-column>
                        <el-table-column prop="Status" label="当前状态"></el-table-column>
                        <el-table-column prop="Content" label="操作内容"></el-table-column>
                    </el-table>
                    <p class="marginBottom">审批流程</p>
                    <div id="container" style="position:relative;width: 100%;height: 300px;"></div>
                </el-col>
                <el-dialog title="提交审批" :visible.sync="approveDialogVisible" width="60%" :append-to-body="true">
                  <el-form :inline="true" label-width="100px">
                    <el-form-item :label="item.label" v-for="(item,index) in approveNodeRow.submitFieldList" :key="index">
                      <el-input v-model="submitField[item.prop]" size="small"></el-input>
                    </el-form-item>
                  </el-form>
                  <span slot="footer" class="dialog-footer">
                    <el-button @click="approveDialogVisible = false">取 消</el-button>
                    <el-button type="primary" @click="submitApprove">保 存</el-button>
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
        name: "FlowPlan",
        props:['enableData'],
        data(){
            return{
                showSteps:false,
                NoRow:"",
                active:0,
                tableData:[],
                ProcessStructure:"",
                stepsList:[],
                LifeTableData:[],
                handleBtns:[],
                graph:null,
                approveDialogVisible:false,
                approveNodeRow:{},
                submitField:{}
            }
        },
        created(){
            this.getTableData()
            this.getWorkflow()
        },
        methods:{
            getWorkflow(){
                var that = this
                var params = {
                  tableName: "TechnologicalProcess",
                  ID:that.enableData.workflowID,
                }
                this.axios.get("/api/CUID",{
                  params: params
                }).then(res => {
                  if(res.data.code === "200"){
                    that.ProcessStructure = JSON.parse(res.data.data.rows[0].ProcessStructure)
                    var firstNodeId = ""
                    that.ProcessStructure.nodes.forEach(item =>{
                        if(item.type === "ellipse"){
                            firstNodeId = item.id
                            that.stepsList.push({
                                title:item.label
                            })
                        }
                    })
                      findLabelById(firstNodeId)
                      function findLabelById(firstNodeId){
                        that.ProcessStructure.edges.forEach(item =>{
                            if(item.source === firstNodeId){
                                that.ProcessStructure.nodes.forEach(j =>{
                                    if(j.type === "rect" || j.type === "diamond"){
                                        if(j.id === item.target){
                                            that.stepsList.push({
                                                title:j.label
                                            })
                                            findLabelById(j.id)
                                        }
                                    }
                                })
                            }
                        })
                      }
                  }else{
                    that.$message({
                      type: 'info',
                      message: res.data.message
                    });
                  }
                })
            },
            getTableData(){
                var that = this
                var params = {
                  tableName: that.enableData.tableName,
                }
                this.axios.get("/api/CUID",{
                  params: params
                }).then(res => {
                  if(res.data.code === "200"){
                    that.tableData = res.data.data.rows
                  }else{
                    that.$message({
                      type: 'info',
                      message: res.data.message
                    });
                  }
                })
            },
            stepDetails(row){
                this.showSteps = true
                this.NoRow = row
                this.getRowInfo()
                this.getLife()
            },
            getRowInfo(){ //根据单号查询基本信息
                var that = this
                var params = {
                    tableName: that.enableData.tableName,
                    [that.enableData.No]:that.NoRow[that.enableData.No]
                }
                this.axios.get("/api/CUID",{
                  params: params
                }).then(res => {
                  if(res.data.code === "200"){
                    that.NoRow = res.data.data.rows[0]
                    that.getNodeBtn()
                    that.init()
                    that.stepsList.forEach((item,index) =>{  //根据当前节点设置步骤条的值
                        if(item.title === that.NoRow[that.enableData.Node]){
                            if(item.type === "triangle"){
                                that.active = 0
                            }else{
                                that.active = index + 1
                            }
                        }
                    })
                  }else{
                    that.$message({
                      type: 'info',
                      message: res.data.message
                    });
                  }
                })
            },
            getLife(){ //获取审批记录
                var that = this
                var params = {
                  tableName:"Life",
                  No:that.NoRow[that.enableData.No],
                }
                this.axios.get("/api/CUID",{
                  params: params
                }).then(res => {
                  if(res.data.code === "200"){
                    that.LifeTableData = res.data.data.rows
                  }else{
                    that.$message({
                      type: 'info',
                      message: res.data.message
                    });
                  }
                })
            },
            //渲染当前节点的操作按钮
            getNodeBtn(){
                var that = this
                var nodeId = "" //当前节点的id
                var targetIdList = [] //目标节点Id列表
                that.ProcessStructure.nodes.forEach(item =>{ //解析工作流 获取当前节点的id
                  if(item.label === that.NoRow.Node){
                    nodeId = item.id
                    that.ProcessStructure.edges.forEach(item =>{  //获取当前节点的目标节点
                      if(item.source === nodeId){
                        targetIdList.push(item.target)
                      }
                    })
                  }
                })
                that.handleBtns = []
                //获取所有目标节点
                that.ProcessStructure.nodes.forEach(item =>{
                  targetIdList.forEach(j =>{
                    if(that.enableData.FlowType){
                        if(that.enableData.FlowType === "task"){
                            if(item.type != "rect"){  //判断是否到任务阶段
                                if(item.id === j){
                                    if(item.type != "triangle"){
                                        that.handleBtns.push(item)
                                    }
                                }
                            }
                        }else if(that.enableData.FlowType === "plan"){
                          if(item.type != "diamond"){  //判断是否到任务阶段
                            if(item.id === j){
                                if(item.type != "triangle"){
                                    that.handleBtns.push(item)
                                }
                            }
                          }
                        }
                    }else{
                        if(item.id === j){
                            if(item.type != "triangle"){
                                that.handleBtns.push(item)
                            }
                        }
                    }
                  })
                })
                //判断默认类型的目标节点是否有驳回子节点，有的话就渲染成按钮
                that.ProcessStructure.edges.forEach(item =>{
                  targetIdList.forEach(j =>{
                    if(item.source === j) { //获取目标节点的目标节点
                        that.ProcessStructure.nodes.forEach(b => {
                            if (b.id === item.target) { //判断获取子节点
                                if (!that.enableData.FlowType) {
                                    if (b.type === "triangle") {
                                        that.handleBtns.push(b)
                                    }
                                }
                            }
                            if(b.id === item.source){
                                if (that.enableData.FlowType) {
                                    if(that.enableData.FlowType === "plan"){
                                        if (b.type === "rect") {
                                            that.ProcessStructure.nodes.forEach(c => {
                                                if(c.id === item.target){
                                                    if (c.type === "triangle") {
                                                        that.handleBtns.push(c)
                                                    }
                                                }
                                            })
                                        }
                                    }else if(that.enableData.FlowType === "task"){
                                        if (b.type === "diamond") {
                                            that.ProcessStructure.nodes.forEach(c => {
                                                if(c.id === item.target){
                                                    if (c.type === "triangle") {
                                                        that.handleBtns.push(c)
                                                    }
                                                }
                                            })
                                        }
                                    }
                                }
                            }
                        })
                    }

                  })
                })
            },
            //审批操作
            approval(row){
                let that = this
                that.ProcessStructure.nodes.forEach(item =>{
                    if(item.id === row.id){
                        if(item.submitFieldList){ //判断是否有提交字段
                            if(item.submitFieldList.length > 0){
                                that.approveDialogVisible = true
                                that.approveNodeRow = row
                                that.submitField = {}
                            }else{
                                that.$confirm('您确定要进行'+ row.label +'操作吗？', '提示', {
                                  distinguishCancelAndClose:true,
                                  type: 'warning'
                                }).then(()  => {
                                  var params = {
                                    tableName:that.enableData.tableName,
                                    ID:that.NoRow.ID,
                                    [that.enableData.Status]:item.state,
                                    [that.enableData.Node]:item.label,
                                  }
                                  that.axios.put("/api/CUID",that.qs.stringify(params)).then(res =>{
                                    if(res.data.code === "200"){
                                      that.$message({
                                        type: 'success',
                                        message: res.data.message
                                      });
                                        that.createLife(item.state,item.label) //添加审批记录
                                        that.getTableData() //更新计划表
                                        that.getRowInfo() //更新当前单号基本信息
                                        that.getLife() //更新审批表
                                    }
                                  },res =>{
                                    console.log("请求错误")
                                  })
                                }).catch(() => {
                                  this.$message({
                                    type: 'info',
                                    message: '已取消操作'
                                  });
                                });
                            }
                        }else{
                            that.$confirm('您确定要进行'+ row.label +'操作吗？', '提示', {
                              distinguishCancelAndClose:true,
                              type: 'warning'
                            }).then(()  => {
                              var params = {
                                tableName:that.enableData.tableName,
                                ID:that.NoRow.ID,
                                [that.enableData.Status]:item.state,
                                [that.enableData.Node]:item.label,
                              }
                              that.axios.put("/api/CUID",that.qs.stringify(params)).then(res =>{
                                if(res.data.code === "200"){
                                  that.$message({
                                    type: 'success',
                                    message: res.data.message
                                  });
                                    that.createLife(item.state,item.label) //添加审批记录
                                    that.getTableData() //更新计划表
                                    that.getRowInfo() //更新当前单号基本信息
                                    that.getLife() //更新审批表
                                }
                              },res =>{
                                console.log("请求错误")
                              })
                            }).catch(() => {
                              this.$message({
                                type: 'info',
                                message: '已取消操作'
                              });
                            });
                        }
                    }
                })
            },
            submitApprove(){ //提交有字段的节点审批
                var that = this
                that.ProcessStructure.nodes.forEach(item =>{
                    if(item.id === that.approveNodeRow.id){
                        var params = {
                            tableName:that.enableData.tableName,
                            ID:that.NoRow.ID,
                            [that.enableData.Status]:item.state,
                            [that.enableData.Node]:item.label,
                        }
                        for(var key in that.submitField){
                            params[key] = that.submitField[key]
                        }
                        this.axios.put("/api/CUID",this.qs.stringify(params)).then(res =>{
                          if(res.data.code === "200"){
                            this.$message({
                              type: 'success',
                              message: res.data.message
                            });
                            that.approveDialogVisible = false
                            that.createLife(item.state,item.label) //添加审批记录
                            that.getTableData() //更新计划表
                            that.getRowInfo() //更新当前单号基本信息
                            that.getLife() //更新审批表
                          }else{
                            this.$message({
                              type: 'info',
                              message: res.data.message
                            });
                          }
                        },res =>{
                          console.log("请求错误")
                        })
                    }
                })
            },
            //添加审批记录
            createLife(Status,label){
                var params = {
                  tableName:"Life",
                  No:this.NoRow.No,
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
                that.$nextTick(() => {
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
                  that.ProcessStructure.nodes.forEach(item =>{ //解析工作流 获取当前节点的id
                    item.style.fill = "#9EC9FF"
                    if(item.label === that.NoRow.Node){
                      item.style.fill = "#e6a23c"
                    }
                  })

                  that.graph.read(that.ProcessStructure);
                })
              },
        }
    }
</script>

<style scoped>

</style>
