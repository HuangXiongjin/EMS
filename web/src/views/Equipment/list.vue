<template>
  <el-row :gutter="15">
    <el-col :span="24" v-if="$route.name != 'EquipmentDetails'">
      <el-form :inline="true">
        <el-row>
          <el-col :span="2">
            <el-form-item label="查询方案："></el-form-item>
          </el-col>
          <el-col :span="22">
            <el-form-item label="设备编号">
              <el-input v-model="TableData.searchField.EquipmentCode" placeholder="请输入设备编号" size="mini" style="width: 150px;"></el-input>
            </el-form-item>
            <el-form-item label="设备名称">
              <el-input v-model="TableData.searchField.EquipmentName" placeholder="请输入设备名称" size="mini" style="width: 150px;"></el-input>
            </el-form-item>
            <el-form-item label="设备等级">
              <el-input v-model="TableData.searchField.Grade" placeholder="请输入设备等级" size="mini" style="width: 150px;"></el-input>
            </el-form-item>
            <el-form-item label="设备状态">
              <el-input v-model="TableData.searchField.Status" placeholder="请输入设备状态" size="mini" style="width: 150px;"></el-input>
            </el-form-item>
            <el-form-item>
              <el-button type="primary" size="mini" @click="getTableData">查询</el-button>
            </el-form-item>
          </el-col>
        </el-row>
      </el-form>
      <div class="platformContainer">
        <el-form :inline="true">
          <el-form-item>
            <el-button type="primary" size="mini" @click="add">添加设备</el-button>
          </el-form-item>
        </el-form>
        <el-table :data="TableData.data" border size="mini" :header-cell-style="{ 'background':'#F5F7FA' }" ref="multipleTable" @select="handleSelect" @selection-change="handleSelectionChange" @row-click="handleRowClick">
          <el-table-column prop="EquipmentCode" label="设备编号">
            <template slot-scope="scope">
              <a href="javascript:;" style="color:#2196F3;" @click="seeDetails(scope.row.EquipmentCode)">{{ scope.row.EquipmentCode }}</a>
            </template>
          </el-table-column>
          <el-table-column prop="EquipmentName" label="设备名称"></el-table-column>
          <el-table-column prop="AssetCode" label="资产编号"></el-table-column>
          <el-table-column prop="LeaveFactoryCode" label="出厂编号"></el-table-column>
          <!--<el-table-column prop="ElectronicCode" label="电子标签码"></el-table-column>-->
          <el-table-column prop="EquipmentType" label="设备类别"></el-table-column>
          <!--<el-table-column prop="Brand" label="品牌"></el-table-column>-->
          <el-table-column prop="Specs" label="规格型号"></el-table-column>
          <el-table-column prop="Unit" label="单位"></el-table-column>
          <el-table-column prop="Source" label="设备来源"></el-table-column>
          <el-table-column prop="Manufacturer" label="供应商"></el-table-column>
          <el-table-column prop="Status" label="设备状态">
            <template slot-scope="scope">
              <span class="btn-block bg-success color-white" v-if="scope.row.Status === '正常'">{{ scope.row.Status }}</span>
              <span class="btn-block bg-orange color-white" v-if="scope.row.Status === '带病运行'">{{ scope.row.Status }}</span>
              <span class="btn-block bg-darkblue color-white" v-if="scope.row.Status === '闲置'">{{ scope.row.Status }}</span>
              <span class="btn-block bg-red color-white" v-if="scope.row.Status === '故障'">{{ scope.row.Status }}</span>
              <span class="btn-block bg-grayblack color-white" v-if="scope.row.Status === '报废'">{{ scope.row.Status }}</span>
            </template>
          </el-table-column>
          <el-table-column prop="Grade" label="设备等级">
            <template slot-scope="scope">
              <span class="btn-block color-white" style="background: #FF5722;" v-if="scope.row.Grade === 'A'">A(关键)</span>
              <span class="btn-block color-white" style="background: #813EDB;" v-if="scope.row.Grade === 'B'">B(重要)</span>
              <span class="btn-block color-white" style="background: #5FB878;"v-if="scope.row.Grade === 'C'">C(一般)</span>
            </template>
          </el-table-column>
          <el-table-column prop="WarrantyTime" label="保修期"></el-table-column>
          <el-table-column prop="UseTime" label="投产时间"></el-table-column>
          <el-table-column prop="IsCalculate" label="计量设备"></el-table-column>
          <!--<el-table-column prop="PurchaseTime" label="购置时间"></el-table-column>-->
          <!--<el-table-column prop="PurchaseMoney" label="购置金额"></el-table-column>-->
          <!--<el-table-column prop="ScrapTime" label="预计报废时间"></el-table-column>-->
          <!--<el-table-column prop="Director" label="负责人"></el-table-column>-->
          <!--<el-table-column prop="Department" label="所属部门"></el-table-column>-->
          <!--<el-table-column prop="Position" label="放置位置"></el-table-column>-->
          <!--<el-table-column prop="IsDepreciation" label="折旧设备"></el-table-column>-->
          <!--<el-table-column prop="NetValue" label="当前净值"></el-table-column>-->
          <!--<el-table-column prop="TechnicalParameter" label="技术参数"></el-table-column>-->
          <!--<el-table-column prop="Comment" label="备注"></el-table-column>-->
          <el-table-column label="操作" fixed="right" width="150">
            <template slot-scope="scope">
              <el-button size="mini" type="warning" @click="Edit(scope.$index, scope.row)">编辑</el-button>
              <el-button size="mini" type="danger" @click="Delete(scope.$index, scope.row)">删除</el-button>
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
        <el-dialog :title="TableData.dialogTitle" :visible.sync="TableData.dialogVisible" width="60%" :append-to-body="true">
          <el-form :inline="true" label-width="80px">
            <el-form-item label="设备编号">
              <el-input v-model="TableData.fieldModel.EquipmentCode" size="small"></el-input>
            </el-form-item>
            <el-form-item label="设备名称">
              <el-input v-model="TableData.fieldModel.EquipmentName" size="small"></el-input>
            </el-form-item>
            <el-form-item label="资产编号">
              <el-input v-model="TableData.fieldModel.AssetCode" size="small"></el-input>
            </el-form-item>
            <el-form-item label="出厂编号">
              <el-input v-model="TableData.fieldModel.LeaveFactoryCode" size="small"></el-input>
            </el-form-item>
            <el-form-item label="设备类别">
              <el-input v-model="TableData.fieldModel.EquipmentType" size="small"></el-input>
            </el-form-item>
            <el-form-item label="品牌">
              <el-input v-model="TableData.fieldModel.Brand" size="small"></el-input>
            </el-form-item>
            <el-form-item label="规格型号">
              <el-input v-model="TableData.fieldModel.Specs" size="small"></el-input>
            </el-form-item>
            <el-form-item label="单位">
              <el-input v-model="TableData.fieldModel.Unit" size="small"></el-input>
            </el-form-item>
            <el-form-item label="设备来源">
              <el-input v-model="TableData.fieldModel.Source" size="small"></el-input>
            </el-form-item>
            <el-form-item label="供应商">
              <el-input v-model="TableData.fieldModel.Manufacturer" size="small"></el-input>
            </el-form-item>
            <el-form-item label="设备状态">
              <el-select v-model="TableData.fieldModel.Status" size="small" placeholder="请选择">
                <el-option label="正常" value="正常"></el-option>
                <el-option label="带病运行" value="带病运行"></el-option>
                <el-option label="闲置" value="闲置"></el-option>
                <el-option label="故障" value="故障"></el-option>
                <el-option label="报废" value="报废"></el-option>
              </el-select>
            </el-form-item>
            <el-form-item label="设备等级">
              <el-select v-model="TableData.fieldModel.Grade" size="small" placeholder="请选择">
                <el-option label="A(关键)" value="A"></el-option>
                <el-option label="B(重要)" value="B"></el-option>
                <el-option label="C(一般)" value="C"></el-option>
              </el-select>
            </el-form-item>
            <el-form-item label="保修期">
              <el-input v-model="TableData.fieldModel.WarrantyTime" size="small"></el-input>
            </el-form-item>
            <el-form-item label="投产时间">
              <el-input v-model="TableData.fieldModel.UseTime" size="small"></el-input>
            </el-form-item>
            <el-form-item label="计量设备">
              <el-input v-model="TableData.fieldModel.IsCalculate" size="small"></el-input>
            </el-form-item>
            <el-form-item label="购置时间">
              <el-input v-model="TableData.fieldModel.PurchaseTime" size="small"></el-input>
            </el-form-item>
            <el-form-item label="购置金额">
              <el-input v-model="TableData.fieldModel.PurchaseMoney" size="small"></el-input>
            </el-form-item>
            <el-form-item label="预计报废时间">
              <el-input v-model="TableData.fieldModel.ScrapTime" size="small"></el-input>
            </el-form-item>
            <el-form-item label="负责人">
              <el-input v-model="TableData.fieldModel.Director" size="small"></el-input>
            </el-form-item>
            <el-form-item label="所属部门">
              <el-input v-model="TableData.fieldModel.Department" size="small"></el-input>
            </el-form-item>
            <el-form-item label="放置位置">
              <el-input v-model="TableData.fieldModel.Position" size="small"></el-input>
            </el-form-item>
            <el-form-item label="折旧设备">
              <el-input v-model="TableData.fieldModel.IsDepreciation" size="small"></el-input>
            </el-form-item>
            <el-form-item label="当前净值">
              <el-input v-model="TableData.fieldModel.NetValue" size="small"></el-input>
            </el-form-item>
            <el-form-item label="技术参数">
              <el-input v-model="TableData.fieldModel.TechnicalParameter" size="small"></el-input>
            </el-form-item>
            <el-form-item label="备注">
              <el-input v-model="TableData.fieldModel.Comment" size="small"></el-input>
            </el-form-item>
          </el-form>
          <span slot="footer" class="dialog-footer">
            <el-button @click="TableData.dialogVisible = false">取 消</el-button>
            <el-button type="primary" @click="save">保 存</el-button>
          </span>
        </el-dialog>
      </div>
    </el-col>
    <el-col :span="24" v-if="$route.name === 'EquipmentDetails'">
      <router-view :key="$route.fullPath"></router-view>
    </el-col>
  </el-row>
</template>

<script>
  export default {
    name: "list",
    data(){
      return{
        TableData:{
          data:[],
          limit: 10,
          offset: 1,
          total: 0,
          multipleSelection: [],
          dialogTitle:"",
          dialogVisible:false,
          searchField:{
            EquipmentCode:"",
            EquipmentName:"",
            Grade:"",
            Status:"",
          },
          fieldModel:{
            ID:"",
            EquipmentCode:"",
            EquipmentName:"",
            AssetCode:"",
            LeaveFactoryCode:"",
            EquipmentType:"",
            Brand:"",
            Specs:"",
            Unit:"",
            Source:"",
            Manufacturer:"",
            Status:"",
            Grade:"",
            WarrantyTime:"",
            UseTime:"",
            IsCalculate:"",
            PurchaseTime:"",
            PurchaseMoney:"",
            ScrapTime:"",
            Director:"",
            Department:"",
            Position:"",
            IsDepreciation:"",
            NetValue:"",
            TechnicalParameter:"",
            Comment:"",
          },
        },
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
      handleSelectionChange(row){
        this.TableData.multipleSelection = row
      },
      handleSelect(selection,row){  //勾选时只能单选
        this.$refs.multipleTable.clearSelection()
        this.$refs.multipleTable.toggleRowSelection(row)
        this.$refs.multipleTable.setCurrentRow(row)
      },
      handleRowClick(row){
        this.$refs.multipleTable.clearSelection()
        this.$refs.multipleTable.toggleRowSelection(row)
      },
      add(){
        this.TableData.dialogVisible = true
        this.TableData.dialogTitle = "添加"
      },
      Edit(index,row){
        this.TableData.dialogVisible = true
        this.TableData.dialogTitle = "修改"
        for(var i in this.TableData.fieldModel){
          this.TableData.fieldModel[i] = row[i]
        }
      },
      Delete(index,row){
        var mulId = [{id:row.ID}]
        var params = {tableName:"Equipment"}
        params.delete_data = JSON.stringify(mulId)
        this.$confirm('确定删除设备 '+ row.EquipmentName +' 吗？', '提示', {
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
            this.getTableData()
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
      save(){
        if(this.TableData.dialogTitle === "添加"){
          var params = {
            tableName:"Equipment",
          }
          for(var i in this.TableData.fieldModel){
            params[i] = this.TableData.fieldModel[i]
          }
          this.axios.post("/api/CUID",this.qs.stringify(params)).then(res =>{
            if(res.data.code === "200"){
              this.$message({
                type: 'success',
                message: res.data.message
              });
              this.TableData.dialogVisible = false
              this.getTableData()
              this.CreateQrcode()
            }else{
              this.$message({
                type: 'info',
                message: res.data.message
              });
            }
          },res =>{
            console.log("请求错误")
          })
        }else if(this.TableData.dialogTitle === "修改"){
          var params = {
            tableName:"Equipment",
          }
          for(var i in this.TableData.fieldModel){
            params[i] = this.TableData.fieldModel[i]
          }
          this.axios.put("/api/CUID",this.qs.stringify(params)).then(res =>{
            if(res.data.code === "200"){
              this.$message({
                type: 'success',
                message: res.data.message
              });
              this.TableData.dialogVisible = false
              this.getTableData()
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
      },
      CreateQrcode(){
        var params = {
          EquipmentCode:this.TableData.fieldModel.EquipmentCode,
        }
        this.axios.post("/api/qrcode",this.qs.stringify(params)).then(res =>{
          if(res.data.code === "1000"){
            this.$message({
              type: 'success',
              message: res.data.msg
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
      seeDetails(EquipmentCode){
        this.$store.commit('setEquipmentCode',EquipmentCode)
        this.$router.push("/EquipmentDetails")
      }
    }
  }
</script>

<style scoped>

</style>
