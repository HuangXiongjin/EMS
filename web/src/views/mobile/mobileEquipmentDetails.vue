<template>
  <el-row>
    <el-col :span="24">
      <mt-header title='基本信息'></mt-header>
      <mt-cell title="设备编码" :value="EquipmentData.EquipmentCode"></mt-cell>
      <mt-cell title="设备名称" :value="EquipmentData.EquipmentName"></mt-cell>
      <mt-cell title="出厂编号" :value="EquipmentData.LeaveFactoryCode"></mt-cell>
      <mt-cell title="规格型号" :value="EquipmentData.Specs"></mt-cell>
      <mt-cell title="品牌" :value="EquipmentData.Brand"></mt-cell>
      <mt-cell title="设备类别" :value="EquipmentData.EquipmentType"></mt-cell>
      <mt-cell title="供应商" :value="EquipmentData.Manufacturer"></mt-cell>
      <mt-cell title="放置位置" :value="EquipmentData.Position"></mt-cell>
    </el-col>
  </el-row>
</template>

<script>
  export default {
    name: "mobileEquipmentDetails",
    data(){
      return {
        EquipmentData:{},
      }
    },
    created(){
      document.title = "设备详情"
      this.getTableData()
    },
    methods:{
      getTableData(){
        var that = this
        var params = {
          tableName: "Equipment",
          EquipmentCode:this.$route.query.EquipmentCode,
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
    }
  }
</script>

<style scoped>

</style>
