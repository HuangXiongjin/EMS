<template>
    <FlowInstance :enableData="keepPlanData"></FlowInstance>
</template>

<script>
  var moment = require('moment');
  import FlowInstance from "../../components/FlowInstance.vue"
    export default {
        name: "upkeepPlan",
        components:{ FlowInstance },
        data(){
            return {
                keepPlanData:{
                    workflowID:"4",
                    tableName:"KeepPlan",
                    tableColumn:[
                      {label:"计划单号",prop:"No"},
                      {label:"流程ID",prop:"TID"},
                      {label:"设备编号",prop:"EquipmentCode"},
                      {label:"设备名称",prop:"KeepEquipment"},
                      {label:"关联保养标准单号",prop:"KeepStandardNo"},
                      {label:"制定人",prop:"PlanUser"},
                      {label:"保养类型",prop:"Type"},
                      {label:"保养周期",prop:"Circle"},
                      {label:"保养项目",prop:"KeepProject"},
                      {label:"提醒时间(天)",prop:"WarningTime"},
                      {label:"接收人",prop:"Receiver"},
                      {label:"备注",prop:"Comment"},
                      {label:"创建时间",prop:"FoundTime"},
                      {label:"下次保养时间",prop:"NextKeepTime"},
                      {label:"当前节点",prop:"Node"},
                      {label:"当前状态",prop:"Status"},
                    ],
                    FlowType:"plan", //默认为空代表不区分流程是计划还是任务 task任务 plan计划
                    No:"No",
                    EquipmentCode:"EquipmentCode",
                    EquipmentName:"KeepEquipment",
                    Time:"FoundTime",
                    User:"PlanUser",
                    Node:"Node",
                    Status:"Status",
                }
            }
        },
        created(){

        },
        methods:{

        }
    }
</script>

<style scoped>

</style>
