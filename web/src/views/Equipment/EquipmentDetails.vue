<template>
  <el-row>
    <el-col :span="24">
      <el-button class="marginBottom" size="mini" @click="returnList">返回列表</el-button>
      <el-tabs v-model="activeName">
        <el-tab-pane label="基本信息" name="1">
          <div class="platformContainer">
            <span>基本信息</span>
            <el-image class="floatRight marginBottom" v-if="EquipmentData.QRCode" style="width: 50px;height: 50px;" :src="'data:;base64,'+EquipmentData.QRCode" :preview-src-list="('data:;base64,'+EquipmentData.QRCode).split() "></el-image>
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
                  <el-image style="width:100px;" :src="'/api/upload_picture?EquipmentCode=' + EquipmentData.EquipmentCode + '&t=' + Math.random()" :preview-src-list="('/api/upload_picture?EquipmentCode=' + EquipmentData.EquipmentCode + '&t=' + Math.random()).split() "></el-image>
                </td>
              </tr>
            </table>
          </div>
        </el-tab-pane>
        <el-tab-pane label="调拨转移记录" name="2">
          <div class="platformContainer">
            <el-form :inline="true">
              <el-form-item v-if="AllocationTableData.firstBtn">
                <el-button type="primary" size="mini" @click="firstBtnEvent">{{ AllocationTableData.firstBtn }}</el-button>
              </el-form-item>
            </el-form>
            <el-table :data="AllocationTableData.data" border size="mini" :header-cell-style="{ 'background':'#F5F7FA' }" ref="multipleTable">
              <el-table-column prop="No" label="调拨单号"></el-table-column>
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
                  <div v-for="(item,index) in AllocationTableData.ProcessStructure.nodes" :key="index">
                    <span class="btn-block color-white" v-if="item.state === scope.row.Status" :style="{ background:item.stateColor }">{{ scope.row.Status }}</span>
                  </div>
                </template>
              </el-table-column>
            </el-table>
            <el-dialog v-if="AllocationTableData.firstBtn" :title="AllocationTableData.firstBtn" :visible.sync="AllocationTableData.dialogVisible" width="60%" :append-to-body="true">
              <el-form :inline="true" label-width="100px">
                <el-form-item label="设备编号">
                  <el-input v-model="EquipmentData.EquipmentCode" size="small" :disabled="true"></el-input>
                </el-form-item>
                <el-form-item label="设备名称">
                  <el-input v-model="EquipmentData.EquipmentName" size="small" :disabled="true"></el-input>
                </el-form-item>
                <el-form-item label="规格型号">
                  <el-input v-model="EquipmentData.Specs" size="small" :disabled="true"></el-input>
                </el-form-item>
                <el-form-item label="调拨单号">
                  <el-input v-model="AllocationTableData.firstBtnSubmit.No" size="small"></el-input>
                </el-form-item>
                <el-form-item label="调拨部门">
                  <el-input v-model="AllocationTableData.firstBtnSubmit.AllocationDepartment" size="small"></el-input>
                </el-form-item>
                <el-form-item label="调出地点">
                  <el-input v-model="AllocationTableData.firstBtnSubmit.AddressOut" size="small"></el-input>
                </el-form-item>
                <el-form-item label="调入地点">
                  <el-input v-model="AllocationTableData.firstBtnSubmit.AddressInto" size="small"></el-input>
                </el-form-item>
                <el-form-item label="调拨原因">
                  <el-input v-model="AllocationTableData.firstBtnSubmit.Comment" size="small"></el-input>
                </el-form-item>
              </el-form>
              <span slot="footer" class="dialog-footer">
                <el-button @click="AllocationTableData.dialogVisible = false">取 消</el-button>
                <el-button type="primary" @click="firstBtnFormSave">保 存</el-button>
              </span>
            </el-dialog>
          </div>
        </el-tab-pane>
        <el-tab-pane label="设备保养计划" name="3">
          <FlowStarted :enableData="keepPlanData"></FlowStarted>
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
        AllocationTableData:{
          tableName:"Allocation",
          workflow:"调拨转移",
          ProcessStructure:"",
          data:[],
          firstBtn:"",
          firstBtnSubmit:{
            No:"",
            AllocationDepartment:"",
            AddressOut:"",
            AddressInto:"",
            Comment:"",
          },
          dialogVisible:false,
        },
        keepPlanData:{
          workflowID:"4",  //工作流引擎ID
          tableName:"KeepPlan", //展示表格的表名
          tableColumn:[
              {label:"计划单号",prop:"No"},
              {label:"设备编号",prop:"EquipmentCode"},
              {label:"设备名称",prop:"KeepEquipment"},
              {label:"关联保养标准单号",prop:"KeepStandardNo"},
              {label:"制定人",prop:"PlanUser"},
              {label:"保养类型",prop:"Type"},
              {label:"保养周期",prop:"Circle"},
              {label:"保养项目",prop:"KeepProject"},
              {label:"提醒时间(天)",prop:"WarningTime"},
              {label:"创建时间",prop:"FoundTime"},
              {label:"下次保养时间",prop:"NextKeepTime"},
              {label:"当前节点",prop:"Node"},
              {label:"当前状态",prop:"Status"},
          ]
        }
      }
    },
    mounted(){
      this.getTableData()
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
            this.getAllocation()
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
      //获取设备调拨申请记录
      getAllocation(){
        var that = this
        var params = {
          tableName: this.AllocationTableData.tableName,
          EquipmentCode:this.EquipmentData.EquipmentCode,
        }
        this.axios.get("/api/CUID",{
          params: params
        }).then(res => {
          if(res.data.code === "200"){
            this.AllocationTableData.data = res.data.data.rows
            this.getWorkflow()
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
          ProcessName:this.AllocationTableData.workflow,
        }
        this.axios.get("/api/CUID",{
          params: params
        }).then(res => {
          if(res.data.code === "200"){
            this.AllocationTableData.ProcessStructure = JSON.parse(res.data.data.rows[0].ProcessStructure)
            this.AllocationTableData.ProcessStructure.nodes.forEach(item =>{
              if(item.type === "ellipse"){
                this.AllocationTableData.firstBtn = item.label
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
      firstBtnEvent(){
        this.AllocationTableData.dialogVisible = true
      },
      firstBtnFormSave(){
        var Status = ""
        this.AllocationTableData.ProcessStructure.nodes.forEach(item =>{
          if(item.label === this.AllocationTableData.firstBtn){
            Status = item.state
          }
        })
        var params = {
          tableName:this.AllocationTableData.tableName,
          EquipmentCode:this.EquipmentData.EquipmentCode,
          EquipmentName:this.EquipmentData.EquipmentName,
          Specs:this.EquipmentData.Specs,
          No:this.AllocationTableData.firstBtnSubmit.No,
          AllocationDepartment:this.AllocationTableData.firstBtnSubmit.AllocationDepartment,
          AddressOut:this.AllocationTableData.firstBtnSubmit.AddressOut,
          AddressInto:this.AllocationTableData.firstBtnSubmit.AddressInto,
          Comment:this.AllocationTableData.firstBtnSubmit.Comment,
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
      },
      //添加审批记录
      createLife(Status){
        var params = {
          tableName:"Life",
          No:this.AllocationTableData.firstBtnSubmit.No,
          Time:moment().format("YYYY-MM-DD HH:ss:mm"),
          User:this.$store.state.UserName,
          Node:this.AllocationTableData.firstBtn,
          Status:Status,
          Content:this.AllocationTableData.firstBtn,
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
