<template>
    <el-row>
        <el-col :span="24">
            <el-steps :active="activeStep" align-center finish-status="success">
              <el-step title="选择保养设备"></el-step>
              <el-step title="选择保养项"></el-step>
              <el-step title="生成保养计划"></el-step>
            </el-steps>
        </el-col>
        <el-col :span="24">
            <div class="platformContainer marginTop">
                <el-form>
                    <el-form-item label="选择设备">
                      <el-cascader :options="EquipmentOptions" v-model="selectEquipment" :props="props" filterable clearable :show-all-levels="false" @change="changeSelectEquipment"></el-cascader>
                    </el-form-item>
                </el-form>
            </div>
        </el-col>
    </el-row>
</template>

<script>
  var moment = require('moment');
    export default {
        name: "upkeepPlan",
        data(){
            return {
                activeStep:0,
                props: { multiple: true },
                EquipmentOptions:[],
                selectEquipment:[]
            }
        },
        created(){
            this.getEquipmentData()
        },
        methods:{
            getEquipmentData(){
                var that = this
                var params = {
                  tableName: "Equipment",
                }
                this.axios.get("/api/CUID",{
                  params: params
                }).then(res => {
                  if(res.data.code === "200"){
                    console.log(res.data.data.rows)
                    that.EquipmentOptions = res.data.data.rows
                  }else{
                    that.$message({
                      type: 'info',
                      message: res.data.message
                    });
                  }
                })
            },
            changeSelectEquipment(){
                console.log(this.selectEquipment)
            }
        }
    }
</script>

<style scoped>

</style>
