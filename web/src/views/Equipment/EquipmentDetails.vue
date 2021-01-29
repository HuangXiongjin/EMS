<template>
  <el-row>
    <el-col :span="24">
      <el-button class="marginBottom" size="mini" @click="returnList">返回列表</el-button>
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
        </table>
      </div>
    </el-col>
  </el-row>
</template>

<script>
  export default {
    name: "EquipmentDetails",
    data(){
      return{
        EquipmentData:{}
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
      }
    }
  }
</script>

<style scoped>

</style>
