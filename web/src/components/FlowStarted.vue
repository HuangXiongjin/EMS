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
                    this.tableData = res.data.data.rows
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
                this.flowNode.submitFieldList.forEach(item =>{ //将提交字段添加到绑定的对象中
                    this.submitField[item.prop] = ""
                })
            },
            Save(){
                console.log(this.submitField)
                var params = {
                  tableName:this.AllocationTableData.tableName,
                  EquipmentCode:this.EquipmentData.EquipmentCode,
                  EquipmentName:this.EquipmentData.EquipmentName,

                  Time:moment().format("YYYY-MM-DD HH:ss:mm"),
                  User:this.$store.state.UserName,
                  Node:this.AllocationTableData.firstBtn,
                  Status:Status,
                }
                this.axios.post("/api/CUID",this.qs.stringify(params)).then(res =>{
                  if(res.data.code === "200"){
                    this.$message({
                      type: 'success',
                      message: res.data.message
                    });
                    this.AllocationTableData.dialogVisible = false
                    this.getAllocation()
                    this.createLife(Status)
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
