<template>
  <el-row :gutter="15">
    <el-col :span="24">
      <el-form :inline="true">
        <el-row>
          <el-col :span="2">
            <el-form-item label="查询方案："></el-form-item>
          </el-col>
          <el-col :span="22">
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
              <a href="javascript:;" style="color:#2196F3;" @click="seeDetails(scope.row.No)">{{ scope.row.No }}</a>
            </template>
          </el-table-column>
          <el-table-column prop="EquipmentName" label="设备名称"></el-table-column>
          <el-table-column prop="EquipmentCode" label="设备编号"></el-table-column>
          <el-table-column prop="Specs" label="规格型号"></el-table-column>
          <el-table-column prop="AllocationDepartment" label="调拨部门"></el-table-column>
          <el-table-column prop="AddressOut" label="调出地点"></el-table-column>
          <el-table-column prop="AddressInto" label="调入地点"></el-table-column>
          <el-table-column prop="Time" label="申请时间"></el-table-column>
          <el-table-column prop="User" label="申请人"></el-table-column>
          <el-table-column prop="Node" label="当前节点"></el-table-column>
          <el-table-column prop="Status" label="审批状态">
            <template slot-scope="scope">
              <span class="btn-block bg-success color-white">{{ scope.row.Status }}</span>
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
    name: "transfer",
    data(){
      return{
        TableData:{
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
          tableName: "Allocation",
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

    }
  }
</script>

<style scoped>

</style>
