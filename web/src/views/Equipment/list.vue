<template>
  <el-row :gutter="15">
    <el-col :span="24">
      <el-form :inline="true">
        <el-row>
          <el-col :span="2">
            <el-form-item label="查询方案："></el-form-item>
          </el-col>
          <el-col :span="22">
            <el-form-item label="设备编号">
              <el-input v-model="TableData.field.EquipmentCode" placeholder="请输入设备编号" size="mini" style="width: 150px;"></el-input>
            </el-form-item>
            <el-form-item label="设备名称">
              <el-input v-model="TableData.field.EquipmentName" placeholder="请输入设备名称" size="mini" style="width: 150px;"></el-input>
            </el-form-item>
            <el-form-item label="设备等级">
              <el-input v-model="TableData.field.Grade" placeholder="请输入设备等级" size="mini" style="width: 150px;"></el-input>
            </el-form-item>
            <el-form-item label="设备状态">
              <el-input v-model="TableData.field.Status" placeholder="请输入设备状态" size="mini" style="width: 150px;"></el-input>
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
          <el-table-column prop="EquipmentCode" label="设备编号"></el-table-column>
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
          <el-table-column prop="Status" label="设备状态"></el-table-column>
          <el-table-column prop="Grade" label="设备等级"></el-table-column>
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
      </div>
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
          field:{
            EquipmentCode:"",
            EquipmentName:"",
            Grade:"",
            Status:"",
          },
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
          EquipmentCode:this.TableData.field.EquipmentCode,
          EquipmentName:this.TableData.field.EquipmentName,
          Grade:this.TableData.field.Grade,
          Status:this.TableData.field.Status,
          limit:this.TableData.limit,
          offset:this.TableData.offset - 1
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

      },
      Edit(index,row){

      },
      Delete(index,row){

      },
    }
  }
</script>

<style scoped>

</style>
