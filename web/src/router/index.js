import Vue from 'vue'
import VueRouter from 'vue-router'

import Index from '@/views/Index'

import Organization from '@/views/system/Organization'
import FactoryManagement from '@/views/system/FactoryManagement'
import Role from '@/views/system/Role'
import TeamGroup from '@/views/system/TeamGroup'
import Personnel from '@/views/system/Personnel'
import Permission from '@/views/system/Permission'
import Log from '@/views/system/Log'
import flowGraph from '@/views/system/flowGraph'
import BuildTable from '@/views/system/BuildTable'
//移动端界面
import mobileEquipmentDetails from '@/views/mobile/mobileEquipmentDetails'

// 设备管理
import list from '@/views/Equipment/list'
import EquipmentDetails from '@/views/Equipment/EquipmentDetails'
import equipmentTree from '@/views/Equipment/equipmentTree'
import Inventory from '@/views/Equipment/Inventory'
import depreciation from '@/views/Equipment/depreciation'
import labelPrinting from '@/views/Equipment/labelPrinting'
import runRecord from '@/views/Equipment/runRecord'

//设备处置
import transfer from '@/views/allocation/transfer'
import scrap from '@/views/allocation/scrap'
import sellOff from '@/views/allocation/sellOff'
import receive from '@/views/allocation/receive'

//维修管理
import maintainStandard from '@/views/maintain/maintainStandard'
import repair from '@/views/maintain/repair'
import Outsourced from '@/views/maintain/Outsourced'
import servicedPlan from '@/views/maintain/servicedPlan'
import servicedTask from '@/views/maintain/servicedTask'

//保养管理
import upkeepStandard from '@/views/upkeep/upkeepStandard'
import upkeepPlan from '@/views/upkeep/upkeepPlan'
import upkeepTask from '@/views/upkeep/upkeepTask'


//点检巡检
import inspectionStandard from '@/views/inspection/inspectionStandard'
import pointInspection from '@/views/inspection/pointInspection'
import pointInspectionLog from '@/views/inspection/pointInspectionLog'
import patrolPlan from '@/views/inspection/patrolPlan'
import patrolTask from '@/views/inspection/patrolTask'

//备品备件
import partsList from '@/views/spareParts/partsList'
import partsReceive from '@/views/spareParts/partsReceive'
import warehouseOut from '@/views/spareParts/warehouseOut'
import warehouseEnter from '@/views/spareParts/warehouseEnter'
import stockTaking from '@/views/spareParts/stockTaking'

//设备监控
import realTimeData from '@/views/monitoring/realTimeData'
import dataReport from '@/views/monitoring/dataReport'

//统计分析
import EquipmentStatistics from '@/views/statistics/EquipmentStatistics'
import upkeepStatistics from '@/views/statistics/upkeepStatistics'
import maintainStatistics from '@/views/statistics/maintainStatistics'
import examineStatistics from '@/views/statistics/examineStatistics'
import warehouseStatistics from '@/views/statistics/warehouseStatistics'
import runingStatistics from '@/views/statistics/runingStatistics'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Index',
    meta:{ title:'系统管理' },
    redirect:'/home',
    component: Index,
    children:[
      {
        path: '/home',
        name: 'home',
        meta:{title:'首页'},
        component: () => import( '../views/home.vue')
      },
      {path:'/Organization',name:'Organization',meta:{ title:'组织架构',type:"系统管理"},component:Organization},
      {path:'/FactoryManagement',name:'FactoryManagement',meta:{ title:'区域管理',type:"系统管理"},component:FactoryManagement},
      {path:'/Role',name:'Role',meta:{ title:'角色权限',type:"系统管理"},component:Role},
      {path:'/TeamGroup',name:'TeamGroup',meta:{ title:'班组管理',type:"系统管理"},component:TeamGroup},
      {path:'/Personnel',name:'Personnel',meta:{ title:'人员管理',type:"系统管理"},component:Personnel},
      {path:'/Permission',name:'Permission',meta:{ title:'权限维护',type:"系统管理"},component:Permission},
      {path:'/Log',name:'Log',meta:{ title:'系统日志',type:"系统管理"},component:Log},
      {path:'/flowGraph',name:'flowGraph',meta:{ title:'工作流管理',type:"系统管理"},component:flowGraph},
      {path:'/BuildTable',name:'BuildTable',meta:{ title:'可视化建表',type:"系统管理"},component:BuildTable},
    ]
  },
  {
    path: '/',
    name: 'Index',
    meta:{ title:'设备管理' },
    component: Index,
    redirect:'/home', //index主页默认加载home页面
    children:[
      {path:'/list',name:'list',meta:{ title:'设备台账',type:"设备管理"},component:list,children:[
          {path:'/EquipmentDetails',name:'EquipmentDetails',meta:{ title:'设备详情'},component:EquipmentDetails},
        ]},
      {path:'/equipmentTree',name:'equipmentTree',meta:{ title:'设备结构树',type:"设备管理"},component:equipmentTree},
      {path:'/Inventory',name:'Inventory',meta:{ title:'设备盘点',type:"设备管理"},component:Inventory},
      {path:'/depreciation',name:'depreciation',meta:{ title:'设备折旧',type:"设备管理"},component:depreciation},
      {path:'/labelPrinting',name:'labelPrinting',meta:{ title:'标签打印',type:"设备管理"},component:labelPrinting},
      {path:'/runRecord',name:'runRecord',meta:{ title:'运行记录',type:"设备管理"},component:runRecord},
    ]
  },
  {
    path: '/',
    name: 'Index',
    meta:{ title:'设备处置' },
    component: Index,
    redirect:'/home',
    children:[
      {path:'/transfer',name:'transfer',meta:{ title:'调拨转移',type:"设备处置"},component:transfer},
      {path:'/scrap',name:'scrap',meta:{ title:'设备报废',type:"设备处置"},component:scrap},
      {path:'/sellOff',name:'sellOff',meta:{ title:'设备变卖',type:"设备处置"},component:sellOff},
      {path:'/receive',name:'receive',meta:{ title:'领用归还',type:"设备处置"},component:receive},
    ]
  },
  {
    path: '/',
    name: 'Index',
    meta:{ title:'维修管理' },
    component: Index,
    redirect:'/home',
    children:[
      {path:'/maintainStandard',name:'maintainStandard',meta:{ title:'检修标准',type:"维修管理"},component:maintainStandard},
      {path:'/repair',name:'repair',meta:{ title:'报修',type:"维修管理"},component:repair},
      {path:'/Outsourced',name:'Outsourced',meta:{ title:'外委维修',type:"维修管理"},component:Outsourced},
      {path:'/servicedPlan',name:'servicedPlan',meta:{ title:'检修计划',type:"维修管理"},component:servicedPlan},
      {path:'/servicedTask',name:'servicedTask',meta:{ title:'检修任务',type:"维修管理"},component:servicedTask},
    ]
  },
  {
    path: '/',
    name: 'Index',
    meta:{ title:'保养管理' },
    component: Index,
    redirect:'/home',
    children:[
      {path:'/upkeepStandard',name:'upkeepStandard',meta:{ title:'保养标准',type:"保养管理"},component:upkeepStandard},
      {path:'/upkeepPlan',name:'upkeepPlan',meta:{ title:'保养计划',type:"保养管理"},component:upkeepPlan},
      {path:'/upkeepTask',name:'upkeepTask',meta:{ title:'保养任务',type:"保养管理"},component:upkeepTask},
    ]
  },
  {
    path: '/',
    name: 'Index',
    meta:{ title:'点检巡检' },
    component: Index,
    redirect:'/home',
    children:[
      {path:'/inspectionStandard',name:'inspectionStandard',meta:{ title:'点巡检标准',type:"点检巡检"},component:inspectionStandard},
      {path:'/pointInspection',name:'pointInspection',meta:{ title:'点检项',type:"点检巡检"},component:pointInspection},
      {path:'/pointInspectionLog',name:'pointInspectionLog',meta:{ title:'点检记录',type:"点检巡检"},component:pointInspectionLog},
      {path:'/patrolPlan',name:'patrolPlan',meta:{ title:'巡检计划',type:"点检巡检"},component:patrolPlan},
      {path:'/patrolTask',name:'patrolTask',meta:{ title:'巡检任务',type:"点检巡检"},component:patrolTask},
    ]
  },
  {
    path: '/',
    name: 'Index',
    meta:{ title:'备品备件' },
    component: Index,
    redirect:'/home',
    children:[
      {path:'/partsList',name:'partsList',meta:{ title:'备件台账',type:"备品备件"},component:partsList},
      {path:'/partsReceive',name:'partsReceive',meta:{ title:'备件领用',type:"备品备件"},component:partsReceive},
      {path:'/warehouseOut',name:'warehouseOut',meta:{ title:'出库管理',type:"备品备件"},component:warehouseOut},
      {path:'/warehouseEnter',name:'warehouseEnter',meta:{ title:'入库管理',type:"备品备件"},component:warehouseEnter},
      {path:'/stockTaking',name:'stockTaking',meta:{ title:'库存盘点',type:"备品备件"},component:stockTaking},
    ]
  },
  {
    path: '/',
    name: 'Index',
    meta:{ title:'设备监控' },
    component: Index,
    redirect:'/home',
    children:[
      {path:'/realTimeData',name:'realTimeData',meta:{ title:'实时数据',type:"设备监控"},component:realTimeData},
      {path:'/dataReport',name:'dataReport',meta:{ title:'数据报表',type:"设备监控"},component:dataReport},
    ]
  },
  {
    path: '/',
    name: 'Index',
    meta:{ title:'统计分析' },
    component: Index,
    redirect:'/home',
    children:[
      {path:'/EquipmentStatistics',name:'EquipmentStatistics',meta:{ title:'设备统计',type:"统计分析"},component:EquipmentStatistics},
      {path:'/upkeepStatistics',name:'upkeepStatistics',meta:{ title:'保养统计',type:"统计分析"},component:upkeepStatistics},
      {path:'/maintainStatistics',name:'maintainStatistics',meta:{ title:'维修统计',type:"统计分析"},component:maintainStatistics},
      {path:'/examineStatistics',name:'examineStatistics',meta:{ title:'维修统计',type:"统计分析"},component:examineStatistics},
      {path:'/warehouseStatistics',name:'warehouseStatistics',meta:{ title:'库存统计',type:"统计分析"},component:warehouseStatistics},
      {path:'/runingStatistics',name:'runingStatistics',meta:{ title:'运行统计',type:"统计分析"},component:runingStatistics},
    ]
  },
  {
    path: '/mobileEquipmentDetails',
    name: 'mobileEquipmentDetails',
    component: mobileEquipmentDetails,
  },
  {
    path: '/login',
    name: 'login',
    component: () => import( '../views/Login.vue')
  },
]

const router = new VueRouter({
  routes
})

export default router
