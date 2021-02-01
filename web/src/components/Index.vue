<template>
  <el-container class="body-container">
    <!-- 头部 -->
    <el-header class="body-head" :style="{ background: themeColor }">
      <div class="head-menu floatLeft">
        <router-link to='/home' style="display: block;height: 100%;">
          <el-image style="width: 80px;height: calc(100% - 18px);margin-top: 10px;transition: all 0.3s ease-out;" :src="require('../assets/logo.png')"></el-image>
        </router-link>
      </div>
      <div class="head-menu floatLeft marginLeft">
        <router-link to='/home'>
          <span class="head-title text-size-20">智能设备管理系统</span>
        </router-link>
      </div>
      <div class="head-menu floatRight">
        <ul>
          <li>
            <el-tooltip class="head-menu-item" effect="dark" content="全屏" placement="bottom">
              <i :class="isFullScreen?'el-icon-aim':'el-icon-full-screen'" @click="getFullCreeen"></i>
            </el-tooltip>
          </li>
          <li>
            <el-tooltip class="head-menu-item" effect="light" placement="bottom">
              <div slot="content">
                <el-color-picker v-model="themeColor" @change="changeTheme"></el-color-picker>
              </div>
              <i class="el-icon-brush"></i>
            </el-tooltip>
          </li>
          <li>
            <el-dropdown class="head-menu-item" trigger="click" @command="handleCommand">
              <span class="el-dropdown-link text-size-16">
                <i class="dotState bg-darkblue"></i>{{ this.$store.state.UserName }}<i class="el-icon-arrow-down el-icon--right text-size-12"></i>
              </span>
              <el-dropdown-menu slot="dropdown">
                <el-dropdown-item command="a">个人信息</el-dropdown-item>
                <el-dropdown-item command="b" style="text-align: center"><i class="fa fa-power-off"></i></el-dropdown-item>
              </el-dropdown-menu>
            </el-dropdown>
            <el-dialog title="用户信息" :visible.sync="dialogUserVisible" :append-to-body="true" width="50%">
              <el-form>
                <el-form-item label="用户名：">{{ userInfo.Name }}</el-form-item>
                <el-form-item label="工号：">{{ userInfo.WorkNumber }}</el-form-item>
                <el-form-item label="最近登录时间：">{{ userInfo.LastLoginTime }}</el-form-item>
                <el-form-item label="权限：">{{ userInfo.Permissions }}</el-form-item>
              </el-form>
              <span slot="footer" class="dialog-footer">
                <el-button @click="dialogUserVisible = false">取 消</el-button>
              </span>
            </el-dialog>
          </li>
        </ul>
      </div>
    </el-header>
    <el-container>
      <!-- 侧边栏 -->
      <el-aside width="220px" class="left-aside">
        <el-row>
          <el-col :span="24">
            <div :style="selfHeight" class="aside-menu">
              <el-menu class="menu-ul" :default-active="defaultActiveUrl" :collapse="menuIsCollapse" :router="true" @select="menuSelect" :active-text-color="themeColor">
                <template v-for="item in systemOptions" :index="item.url">
                  <el-menu-item v-if="!item.mainMenu" :index="item.url"><i :class="item.icon"></i><span slot="title">{{ item.title }}</span></el-menu-item>
                  <el-submenu v-if="item.mainMenu" :index="item.title">
                    <template slot="title"><i :class="item.icon"></i><span>{{ item.title }}</span></template>
                    <el-menu-item v-for="(child,childIndex) in item.mainMenu" :key="childIndex" :index="child.url"><span style="margin-left:10px;">{{child.title}}</span></el-menu-item>
                  </el-submenu>
                </template>
              </el-menu>
            </div>
            <div class="aside-foot">
              <el-button :icon="sideIcon" size="mini" circle @click="iconToggle" :style="{ background: themeColor }"></el-button>
            </div>
          </el-col>
        </el-row>
      </el-aside>
      <!-- 页面主体 -->
      <el-container>
        <el-header style="height: 40px;padding-top:10px;">
          <el-breadcrumb separator="/" style="line-height: 40px;">
            <el-breadcrumb-item v-for="(item,index) in breadList" :key="index" :to="{ path: item.path }">{{ item.meta.title }}</el-breadcrumb-item>
          </el-breadcrumb>
        </el-header>
        <el-main style="clear: both;">
          <transition name="move" mode="out-in">
           <!--渲染子页面-->
            <router-view :key="$route.fullPath"></router-view>
          </transition>
        </el-main>
      </el-container>
    </el-container>
  </el-container>
</template>

<script>
  var moment = require('moment');
  import screenfull from "screenfull"
  export default {
    name: 'Index',
    data () {
      return {
        selfHeight:{ //自适应高度
          height:''
        },
        menuIsCollapse: false, //左侧菜单栏是否缩进了
        sideIcon:'el-icon-arrow-left', //左侧菜单栏缩进点击切换图标
        systemOptions:[
          {title: '设备管理',icon:"el-icon-document",mainMenu:[
              {title:"设备台账",url:"/list"},
              {title:"设备结构树",url:"/equipmentTree"},
              {title:"设备盘点",url:"/Inventory"},
              {title:"设备折旧",url:"/depreciation"},
              {title:"标签打印",url:"/labelPrinting"},
              {title:"运行记录",url:"/runRecord"},
            ]},
          {title: '设备处置',icon:"fa fa-exchange",mainMenu:[
              {title:"调拨转移",url:"/transfer"},
              {title:"设备报废",url:"/scrap"},
              {title:"设备变卖",url:"/sellOff"},
              {title:"领用归还",url:"/receive"},
            ]},
          {title: '维修管理',icon:"fa fa-wrench",mainMenu:[
              {title:"检修标准",url:"/maintainStandard"},
              {title:"报修",url:"/repair"},
              {title:"外委维修",url:"/Outsourced"},
              {title:"检修计划",url:"/servicedPlan"},
              {title:"检修任务",url:"/servicedTask"},
            ]},
          {title: '保养管理',icon:"fa fa-history",mainMenu:[
              {title:"保养标准",url:"/upkeepStandard"},
              {title:"保养计划",url:"/upkeepPlan"},
              {title:"保养任务",url:"/upkeepTask"},
            ]},
          {title: '点检巡检',icon:"fa fa-compass",mainMenu:[
              {title:"点巡检标准",url:"/inspectionStandard"},
              {title:"点检项",url:"/pointInspection"},
              {title:"点检记录",url:"/pointInspectionLog"},
              {title:"巡检计划",url:"/patrolPlan"},
              {title:"巡检任务",url:"/patrolTask"},
            ]},
          {title: '备品备件',icon:"fa fa-archive",mainMenu:[
              {title:"备件台账",url:"/partsList"},
              {title:"备件领用",url:"/partsReceive"},
              {title:"出库管理",url:"/warehouseOut"},
              {title:"入库管理",url:"/warehouseEnter"},
              {title:"库存盘点",url:"/stockTaking"},
            ]},
          {title: '设备监控',icon:"el-icon-view",mainMenu:[
              {title:"实时数据",url:"/realTimeData"},
              {title:"数据报表",url:"/dataReport"},
            ]},
          {title: '统计分析',icon:"fa fa-bar-chart",mainMenu:[
              {title:"设备统计",url:"/EquipmentStatistics"},
              {title:"保养统计",url:"/upkeepStatistics"},
              {title:"维修统计",url:"/maintainStatistics"},
              {title:"点检统计",url:"/examineStatistics"},
              {title:"库存统计",url:"/warehouseStatistics"},
              {title:"运行统计",url:"/runingStatistics"},
            ]},
          {title: '系统管理',icon:"el-icon-s-tools",mainMenu:[
              {title:"组织架构",url:"/Organization"},
              {title:"区域管理",url:"/FactoryManagement"},
              {title:"角色权限",url:"/Role"},
              {title:"班组管理",url:"/TeamGroup"},
              {title:"人员管理",url:"/Personnel"},
              {title:"权限维护",url:"/Permission"},
              {title:"流程管理",url:"/flowGraph"},
              {title:"可视化建表",url:"/BuildTable"},
              {title:"系统日志",url:"/Log"}
            ]},
        ],
        defaultActiveUrl:"",
        dialogUserVisible:false, //是否弹出个人信息
        userInfo:{},
        isFullScreen:false, //是否全屏
        themeColor:"",
        breadList:[],
      }
    },
    mounted(){
      if(localStorage.getItem('theme')){
        this.themeColor = localStorage.getItem('theme')
      }else{
        this.themeColor = "#4881e6"
      }
    },
    created(){
      document.title = "智能设备管理系统"
      window.addEventListener('resize', this.getMenuHeight);
      this.getMenuHeight()
      if(sessionStorage.getItem("LoginStatus")) {
        this.$store.commit('setUser',sessionStorage.getItem('WorkNumber'))
      }else{
        this.$router.push("/login");
      }
      this.getBreadcrumb()
      if(this.$route.path === "/home"){ //判断当前路由 设置当前路由对应的菜单
        this.defaultActiveUrl = ""
      }else{
        this.systemOptions.forEach((menu,i) =>{
          if(menu.title === this.$route.meta.type){
            this.defaultActiveUrl = this.$route.path
          }
        })
      }
    },
    destroyed() {

    },
    watch:{
      $route:{
        handler(val,oldval){
          this.defaultActiveUrl = val.path
          this.getBreadcrumb();
        },
        deep: true,
      }
    },
    methods:{
      getMenuHeight(){
        if(this.menuIsCollapse){
          this.selfHeight.height = window.innerHeight - 180+'px';
        }else{
          this.selfHeight.height = window.innerHeight - 180+'px';
        }
      },
      menuSelect(url,title){  //点击菜单跳转时  添加query参数避免相同路由跳转时报错
        this.$router.push({
          query:moment()
        })
      },
      handleCommand(command) {  //判断用户下拉点击
        if(command === "a"){
          this.dialogUserVisible = true
          this.userInfo.LastLoginTime = sessionStorage.getItem('LastLoginTime')
          this.userInfo.WorkNumber = sessionStorage.getItem('WorkNumber')
          this.userInfo.Name = sessionStorage.getItem('UserName')
          this.userInfo.Permissions = JSON.parse(sessionStorage.getItem('Permissions')).join('，')
        }else if(command === "b"){
          this.$store.commit('removeUser')
          this.$router.replace("/login")
        }
      },
      iconToggle() {  //折叠菜单
        this.menuIsCollapse = !this.menuIsCollapse
        this.getMenuHeight()
        if(this.menuIsCollapse){
          this.sideIcon = 'el-icon-arrow-right'
          $(".left-aside").animate({"width":"64px"})
        }else{
          this.sideIcon = 'el-icon-arrow-left'
          $(".left-aside").animate({"width":"220px"})
        }
      },
      getFullCreeen () {  //全屏
        if (screenfull.isEnabled) {
          screenfull.toggle()
          if(screenfull.isFullscreen){
            this.isFullScreen = false
          }else{
            this.isFullScreen = true
          }
        }
      },
      changeTheme(value){
        this.themeColor = value
        localStorage.setItem('theme', value);
      },
      getBreadcrumb(){
        if(this.$route.name != "home") {
          this.breadList = [{ path: "/home", meta: { title: "首页" } }].concat(this.$route.matched);
        }else{
          this.breadList = [{ path: "/home",name:"home", meta: { title: "首页" } }]
        }
      },
    }
  }
</script>
<style lang="less" scoped>

</style>
