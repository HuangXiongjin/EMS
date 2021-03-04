<template>
  <el-row>
    <el-col :span="24">
      <el-button class="marginBottom" size="mini" @click="returnList">返回列表</el-button>
      <el-tabs v-model="activeName">
        <el-tab-pane label="基本信息" name="1">
          <div class="platformContainer">
            <el-row :gutter="20">
              <el-col :span="12">
                <span>基本信息</span>
                <el-image class="floatRight marginBottom" v-if="EquipmentData.QRCode" style="width: 50px;height: 50px;" :src="'data:;base64,'+EquipmentData.QRCode" :preview-src-list="('data:;base64,'+EquipmentData.QRCode).split()"></el-image>
                <table class="elementTable text-size-14">
                  <tr>
                    <td>设备编号</td>
                    <td>{{ EquipmentData.EquipmentCode }}</td>
                    <td>设备名称</td>
                    <td>{{ EquipmentData.EquipmentName }}</td>
                    <td>资产编号</td>
                    <td>{{ EquipmentData.AssetCode }}</td>
                    <td>出厂编号</td>
                    <td>{{ EquipmentData.LeaveFactoryCode }}</td>
                  </tr>
                  <tr>
                    <td>设备类别</td>
                    <td>{{ EquipmentData.EquipmentType }}</td>
                    <td>品牌</td>
                    <td>{{ EquipmentData.Brand }}</td>
                    <td>规格型号</td>
                    <td>{{ EquipmentData.Specs }}</td>
                    <td>单位</td>
                    <td>{{ EquipmentData.Unit }}</td>
                  </tr>
                  <tr>
                    <td>设备来源</td>
                    <td>{{ EquipmentData.Source }}</td>
                    <td>供应商</td>
                    <td>{{ EquipmentData.Manufacturer }}</td>
                    <td>保修期</td>
                    <td>{{ EquipmentData.WarrantyTime }}</td>
                    <td>当前净值</td>
                    <td>{{ EquipmentData.NetValue }}</td>
                  </tr>
                    <td>设备状态</td>
                    <td colspan="3">
                      <span class="btn-block bg-success color-white" v-if="EquipmentData.Status === '正常'">{{ EquipmentData.Status }}</span>
                      <span class="btn-block bg-orange color-white" v-if="EquipmentData.Status === '带病运行'">{{ EquipmentData.Status }}</span>
                      <span class="btn-block bg-darkblue color-white" v-if="EquipmentData.Status === '闲置'">{{ EquipmentData.Status }}</span>
                      <span class="btn-block bg-red color-white" v-if="EquipmentData.Status === '故障'">{{ EquipmentData.Status }}</span>
                      <span class="btn-block bg-grayblack color-white" v-if="EquipmentData.Status === '报废'">{{ EquipmentData.Status }}</span>
                    </td>
                    <td>设备等级</td>
                    <td colspan="3">
                      <span class="btn-block color-white" style="background: #FF5722;" v-if="EquipmentData.Grade === 'A'">A(关键)</span>
                      <span class="btn-block color-white" style="background: #813EDB;" v-if="EquipmentData.Grade === 'B'">B(重要)</span>
                      <span class="btn-block color-white" style="background: #5FB878;"v-if="EquipmentData.Grade === 'C'">C(一般)</span>
                    </td>
                  <tr>
                    <td>购置时间</td>
                    <td>{{ EquipmentData.PurchaseTime }}</td>
                    <td>购置金额</td>
                    <td>{{ EquipmentData.PurchaseMoney }}</td>
                    <td>投产时间</td>
                    <td>{{ EquipmentData.UseTime }}</td>
                    <td>预计报废时间</td>
                    <td>{{ EquipmentData.ScrapTime }}</td>
                  </tr>
                  <tr>
                    <td>负责人</td>
                    <td colspan="7">{{ EquipmentData.Director }}</td>
                  </tr>
                  <tr>
                    <td>所属部门</td>
                    <td colspan="7">{{ EquipmentData.Department }}</td>
                  </tr>
                  <tr>
                    <td>放置位置</td>
                    <td colspan="7">{{ EquipmentData.Position }}</td>
                  </tr>
                  <tr>
                    <td>折旧设备</td>
                    <td colspan="3">{{ EquipmentData.IsDepreciation }}</td>
                    <td>计量设备</td>
                    <td colspan="3">{{ EquipmentData.IsCalculate }}</td>
                  </tr>
                  <tr>
                    <td>技术参数</td>
                    <td colspan="7">{{ EquipmentData.TechnicalParameter }}</td>
                  </tr>
                  <tr>
                    <td>备注</td>
                    <td colspan="7">{{ EquipmentData.Comment }}</td>
                  </tr>
                  <tr>
                    <td>图片</td>
                    <td colspan="7">
                      <el-image style="width: 100px; min-height: 100px" :src="'/api/upload_picture?EquipmentCode=' + EquipmentData.EquipmentCode" :preview-src-list="('/api/upload_picture?EquipmentCode=' + EquipmentData.EquipmentCode + '&t=' + Math.random()).split() "></el-image>
                    </td>
                  </tr>
                </table>
              </el-col>
              <el-col :span="12">
                <p class="marginBottom">保养项目</p>
                <el-form :inline="true">
                    <p class="marginBottom">
                      <el-button type="primary" size="mini" @click="addKeepProject">添加</el-button>
                    </p>
                </el-form>
                <el-table class="marginBottom" :data="KeepProjectTableData" border size="mini" :header-cell-style="{ 'background':'#F5F7FA' }">
                  <el-table-column prop="EquipmentCode" label="设备编号"></el-table-column>
                  <el-table-column prop="Circle" label="保养周期"></el-table-column>
                  <el-table-column prop="KeepProject" label="保养项目">
                    <template slot-scope="scope">
                      <p v-for="(item,index) in scope.row.KeepProject.split(',')" :key="index">-{{ item }}</p>
                    </template>
                  </el-table-column>
                  <el-table-column prop="Name" label="制定人"></el-table-column>
                  <el-table-column prop="Time" label="制定时间"></el-table-column>
                  <el-table-column label="操作" fixed="right" width="150">
                    <template slot-scope="scope">
                      <el-button size="mini" type="warning" @click="editKeepProject(scope.row)">修改</el-button>
                      <el-button size="mini" type="danger" @click="DeleteKeepProject(scope.row)">删除</el-button>
                    </template>
                  </el-table-column>
                </el-table>
                <el-dialog :title="KeepProjectTitle" :visible.sync="KeepProjectDialogVisible" width="50%" :append-to-body="true">
                  <el-form label-width="100px">
                    <el-form-item label="设备编号">
                      <el-input v-model="KeepProjectField.EquipmentCode" size="small" :disabled="true"></el-input>
                    </el-form-item>
                    <el-form-item label="保养周期">
                      <el-col :span="10">
                        <el-input type="number" v-model="KeepProjectField.CircleNum" size="small"></el-input>
                      </el-col>
                      <el-col :span="10">
                        <el-select v-model="KeepProjectField.CircleType" placeholder="请选择周期类型">
                          <el-option label="日" value="日"></el-option>
                          <el-option label="周" value="周"></el-option>
                          <el-option label="月" value="月"></el-option>
                          <el-option label="季" value="季"></el-option>
                          <el-option label="年" value="年"></el-option>
                        </el-select>
                      </el-col>
                    </el-form-item>
                    <el-form-item label="保养项目">
                      <el-tag :key="tag" v-for="tag in KeepProjectField.KeepProject" closable :disable-transitions="false" @close="handleClose(tag)">{{tag}}</el-tag>
                      <el-input class="input-new-tag" v-if="inputVisible" v-model="inputValue" ref="saveTagInput" size="small" @keyup.enter.native="handleInputConfirm" @blur="handleInputConfirm"></el-input>
                      <el-button v-else class="button-new-tag" size="small" @click="showInput">+ 保养项目</el-button>
                    </el-form-item>
                  </el-form>
                  <span slot="footer" class="dialog-footer">
                    <el-button @click="KeepProjectDialogVisible = false">取 消</el-button>
                    <el-button type="primary" @click="saveKeepProject">保 存</el-button>
                  </span>
                </el-dialog>
              </el-col>
            </el-row>
          </div>
        </el-tab-pane>
        <el-tab-pane label="调拨转移记录" name="2">
          <FlowStarted :enableData="AllocationData"></FlowStarted>
        </el-tab-pane>
      </el-tabs>
    </el-col>
  </el-row>
</template>

<script>
  var moment = require('moment');
  import FlowStarted from "../../components/FlowStarted.vue"
  export default {
    name: "EquipmentDetails",
    components:{
      FlowStarted
    },
    data(){
      return{
        EquipmentData:{},
        activeName:"1",
        AllocationData:{
          workflowID:"3",  //工作流引擎ID
          tableName:"Allocation", //展示表格的表名
          tableColumn:[
              {label:"计划单号",prop:"No"},
              {label:"设备编号",prop:"EquipmentCode"},
              {label:"设备名称",prop:"EquipmentName"},
              {label:"调拨部门",prop:"AllocationDepartment"},
              {label:"调出地点",prop:"AddressOut"},
              {label:"调入地点",prop:"AddressInto"},
              {label:"调拨原因",prop:"Comment"},
              {label:"申请时间",prop:"Time"},
              {label:"申请人",prop:"User"},
              {label:"当前节点",prop:"Node"},
              {label:"当前状态",prop:"Status"},

          ],
          No:"No",
          EquipmentCode:"EquipmentCode",
          EquipmentName:"EquipmentName",
          Time:"Time",
          User:"User",
          Node:"Node",
          Status:"Status",
        },
        // keepPlanData:{
        //   workflowID:"4",
        //   tableName:"KeepPlan",
        //   tableColumn:[
        //       {label:"计划单号",prop:"No"},
        //       {label:"流程ID",prop:"TID"},
        //       {label:"设备编号",prop:"EquipmentCode"},
        //       {label:"设备名称",prop:"KeepEquipment"},
        //       {label:"关联保养标准单号",prop:"KeepStandardNo"},
        //       {label:"制定人",prop:"PlanUser"},
        //       {label:"保养类型",prop:"Type"},
        //       {label:"保养周期",prop:"Circle"},
        //       {label:"保养项目",prop:"KeepProject"},
        //       {label:"提醒时间(天)",prop:"WarningTime"},
        //       {label:"创建时间",prop:"FoundTime"},
        //       {label:"下次保养时间",prop:"NextKeepTime"},
        //       {label:"当前节点",prop:"Node"},
        //       {label:"当前状态",prop:"Status"},
        //   ],
        //   workflowIDField:"TID",
        //   No:"No",
        //   EquipmentCode:"EquipmentCode",
        //   EquipmentName:"KeepEquipment",
        //   Time:"FoundTime",
        //   User:"PlanUser",
        //   Node:"Node",
        //   Status:"Status",
        // },
        KeepProjectTableData:[],
        KeepProjectTitle:"",
        KeepProjectDialogVisible:false,
        KeepProjectField:{
          ID:"",
          EquipmentCode:"",
          CircleNum:"",
          CircleType:"",
          KeepProject:[]
        },
        inputVisible: false,
        inputValue: "",
      }
    },
    mounted(){
      this.getTableData()
      this.getKeepProjectData()
    },
    methods:{
      getTableData(){
        var that = this
        var params = {
          tableName: "Equipment",
          EquipmentCode:this.$store.state.EquipmentCode,
        }
        this.axios.get("/api/CUID",{
          params: params
        }).then(res => {
          if(res.data.code === "200"){
            this.EquipmentData = res.data.data.rows[0]
          }else{
            that.$message({
              type: 'info',
              message: res.data.message
            });
          }
        })
      },
      returnList(){
        this.$router.push("/list")
      },
      getKeepProjectData(){
        var params = {
          tableName:"KeepProject",
          EquipmentCode:this.$store.state.EquipmentCode
        }
        this.axios.get("/api/CUID",{
          params: params
        }).then(res =>{
          if(res.data.code === "200"){
            this.KeepProjectTableData = res.data.data.rows
          }else{
            that.$message({
              type: 'info',
              message: res.data.message
            });
          }
        },res =>{
          console.log("请求错误")
        })
      },
      addKeepProject(){
        this.KeepProjectDialogVisible = true
        this.KeepProjectTitle = "添加"
        this.KeepProjectField.ID = ""
        this.KeepProjectField.EquipmentCode = this.$store.state.EquipmentCode
        this.KeepProjectField.CircleNum = "1"
        this.KeepProjectField.CircleType = "日"
        this.KeepProjectField.KeepProject = []
      },
      editKeepProject(row){
        this.KeepProjectDialogVisible = true
        this.KeepProjectTitle = "修改"
        this.KeepProjectField.ID = row.ID
        this.KeepProjectField.EquipmentCode = row.EquipmentCode
        this.KeepProjectField.CircleNum = row.Circle.match(/(\d{1,3})+(?:\.\d+)?/g).toString()
        this.KeepProjectField.CircleType = row.Circle.match(/[\u4e00-\u9fa5]/g).toString()
        this.KeepProjectField.KeepProject = row.KeepProject.split(",")
      },
      saveKeepProject(){
        if(this.KeepProjectTitle === "添加"){
            if(Number(this.KeepProjectField.CircleNum) > 0 && this.KeepProjectField.CircleType){
              var params = {
                tableName:"KeepProject",
                ID:this.KeepProjectField.ID,
                EquipmentCode:this.KeepProjectField.EquipmentCode,
                Circle:this.KeepProjectField.CircleNum + this.KeepProjectField.CircleType,
                KeepProject:this.KeepProjectField.KeepProject.join(","),
                Name:this.$store.state.UserName,
                Time:moment().format("YYYY-MM-DD HH:ss:mm"),
              }
              this.axios.post("/api/CUID",this.qs.stringify(params)).then(res =>{
                if(res.data.code === "200"){
                  this.$message({
                    type: 'success',
                    message: res.data.message
                  });
                  this.getKeepProjectData()
                }else{
                  this.$message({
                    type: 'info',
                    message: res.data.message
                  });
                }
                this.KeepProjectDialogVisible = false
              },res =>{
                console.log("请求错误")
              })
            }else{
              this.$message({
                type: 'info',
                message: "请输入正确的保养周期"
              });
            }
        }else if(this.KeepProjectTitle === "修改"){
            if(Number(this.KeepProjectField.CircleNum) > 0 && this.KeepProjectField.CircleType) {
                var params = {
                    tableName: "KeepProject",
                    ID: this.KeepProjectField.ID,
                    Circle: this.KeepProjectField.CircleNum + this.KeepProjectField.CircleType,
                    KeepProject: this.KeepProjectField.KeepProject.join(","),
                }
                this.axios.put("/api/CUID", this.qs.stringify(params)).then(res => {
                    if (res.data.code === "200") {
                        this.$message({
                            type: 'success',
                            message: res.data.message
                        });
                        this.getKeepProjectData()
                    } else {
                        this.$message({
                            type: 'info',
                            message: res.data.message
                        });
                    }
                    this.KeepProjectDialogVisible = false
                }, res => {
                    console.log("请求错误")
                })
            }
        }
      },
      DeleteKeepProject(row){
        var mulId = [{id:row.ID}]
        var params = {tableName:"KeepProject"}
        params.delete_data = JSON.stringify(mulId)
        this.$confirm('确定删除此保养项吗？', '提示', {
          distinguishCancelAndClose:true,
          type: 'warning'
        }).then(()  => {
          this.axios.delete("/api/CUID",{
            params:params
          }).then(res =>{
            if(res.data.code === "200"){
              this.$message({
                type: 'success',
                message: res.data.message
              });
            }
            this.getKeepProjectData()
          },res =>{
            console.log("请求错误")
          })
        }).catch(() => {
          this.$message({
            type: 'info',
            message: '已取消删除'
          });
        });
      },
      handleClose(tag) {
        this.KeepProjectField.KeepProject.splice(this.KeepProjectField.KeepProject.indexOf(tag), 1);
      },
      showInput() {
        this.inputVisible = true;
        this.$nextTick(_ => {
          this.$refs.saveTagInput.$refs.input.focus();
        });
      },
      handleInputConfirm() {
        let inputValue = this.inputValue;
        if (inputValue) {
          this.KeepProjectField.KeepProject.push(inputValue);
        }
        this.inputVisible = false;
        this.inputValue = '';
      },

    }
  }
</script>

<style scoped>
  .el-tag + .el-tag {
    margin-left: 10px;
  }
  .button-new-tag {
    margin-left: 10px;
    height: 32px;
    line-height: 30px;
    padding-top: 0;
    padding-bottom: 0;
  }
  .input-new-tag {
    width: 150px;
    margin-left: 10px;
    vertical-align: bottom;
  }
</style>
