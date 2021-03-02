<template>
    <div class="platformContainer">
        <el-form :inline="true">
          <el-form-item v-if="flowNode.label">
            <el-button type="primary" size="mini" @click="subBottonEvent">{{ flowNode.label }}</el-button>
          </el-form-item>
        </el-form>
        <el-table :data="tableData" border size="mini" :header-cell-style="{ 'background':'#F5F7FA' }" ref="multipleTable">
          <el-table-column v-for="(item,index) in enableData.tableColumn" :prop="item.prop" :label="item.label"></el-table-column>
        </el-table>
        <el-dialog v-if="flowNode" :title="flowNode.label" :visible.sync="dialogVisible" width="60%" :append-to-body="true">
          <el-form :inline="true" label-width="100px">
            <el-form-item label="设备编号">
              <el-input v-model="EquipmentRow.EquipmentCode" size="small" :disabled="true"></el-input>
            </el-form-item>
            <el-form-item label="设备名称">
              <el-input v-model="EquipmentRow.EquipmentName" size="small" :disabled="true"></el-input>
            </el-form-item>
            <el-form-item label="计划单号" v-if="enableData.hasOwnProperty('No')">
              <el-input v-model="submitField[enableData.No]" size="small"></el-input>
            </el-form-item>
            <el-form-item :label="item.label" v-for="(item,index) in flowNode.submitFieldList" :key="index">
              <el-input v-model="submitField[item.prop]" size="small"></el-input>
            </el-form-item>
          </el-form>
          <span slot="footer" class="dialog-footer">
            <el-button @click="dialogVisible = false">取 消</el-button>
            <el-button type="primary" @click="Save">保 存</el-button>
          </span>
        </el-dialog>
    </div>
</template>

<script>
    var moment = require('moment');
    export default {
        name: "FlowStarted",
        props:['enableData'],
        data(){
            return{
                flowNode:{}, //流程结构
                EquipmentRow:{}, //已选设备的基本信息
                tableData:[], //表格数据
                dialogVisible:false,
                submitField:{}
            }

        },
        created(){
            this.getWorkflow()
            this.getEqInfo()
        },
        methods:{
            getEqInfo(){
                var that = this
                var params = {
                  tableName: "Equipment",
                  EquipmentCode:that.$store.state.EquipmentCode,
                }
                this.axios.get("/api/CUID",{
                  params: params
                }).then(res => {
                  if(res.data.code === "200"){
                    that.EquipmentRow = res.data.data.rows[0]
                    that.getTableData()
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
                  EquipmentCode:that.$store.state.EquipmentCode,
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
                    JSON.parse(res.data.data.rows[0].ProcessStructure).nodes.forEach(item =>{
                      if(item.type === "ellipse"){
                        that.flowNode = item
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
            subBottonEvent(){
                this.dialogVisible = true
            },
            Save(){
                var that = this
                var params = {
                  tableName:that.enableData.tableName,
                }
                if(that.enableData.hasOwnProperty("workflowIDField")){
                    params[that.enableData.workflowIDField] = that.enableData.workflowID
                }
                if(that.enableData.hasOwnProperty("EquipmentCode")){
                    params[that.enableData.EquipmentCode] = that.EquipmentRow.EquipmentCode
                }
                if(that.enableData.hasOwnProperty("EquipmentName")){
                    params[that.enableData.EquipmentName] = that.EquipmentRow.EquipmentName
                }
                if(that.enableData.hasOwnProperty("Time")){
                    params[that.enableData.Time] = moment().format("YYYY-MM-DD HH:ss:mm")
                }
                if(that.enableData.hasOwnProperty("User")){
                    params[that.enableData.User] = that.$store.state.UserName
                }
                if(that.enableData.hasOwnProperty("Node")){
                    params[that.enableData.Node] = that.flowNode.label
                }
                if(that.enableData.hasOwnProperty("Status")){
                    params[that.enableData.Status] = that.flowNode.state
                }
                for(var key in that.submitField){
                    params[key] = that.submitField[key]
                }
                this.axios.post("/api/CUID",this.qs.stringify(params)).then(res =>{
                  if(res.data.code === "200"){
                    this.$message({
                      type: 'success',
                      message: res.data.message
                    });
                    this.dialogVisible = false
                    this.getTableData()
                    this.createLife()
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
            //添加审批记录
            createLife(){
                var that = this
                var params = {
                  tableName:"Life",
                  No:that.submitField[that.enableData.No],
                  RID:that.enableData.workflowID,
                  Time:moment().format("YYYY-MM-DD HH:ss:mm"),
                  User:that.$store.state.UserName,
                  Node:that.flowNode.label,
                  Status:that.flowNode.state,
                  Content:that.flowNode.label,
                }
                this.axios.post("/api/CUID",this.qs.stringify(params)).then(res =>{
                  if(res.data.code === "200"){
                    this.$message({
                      type: 'success',
                      message: res.data.message
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
            }
        }
    }
</script>

<style scoped>

</style>
