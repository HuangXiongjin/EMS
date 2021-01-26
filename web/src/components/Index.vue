<template>
  <el-container class="body-container">
    <!-- 头部 -->
    <el-header class="body-head">
      <div class="head-menu floatLeft">
        <router-link to='/home'><span class="head-title">设备管理系统</span></router-link>
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
                <ul>
                  <li class="themeItem" v-for="(item,index) in themeList" :class="{ active:item.value===themeValue }" :key="index" :style="{background:item.color}" @click="changeTheme(item.value)"></li>
                </ul>
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
            <el-menu class="menu-ul" :default-active="defaultActiveUrl" :collapse="menuIsCollapse" :router="true" @select="menuSelect">
              <template v-for="item in mainMenu" :index="item.url">
                <el-menu-item v-if="!item.children" :index="item.url"><i :class="item.icon"></i><span slot="title">{{ item.title }}</span></el-menu-item>
                <el-submenu v-if="item.children" :index="item.title">
                  <template slot="title"><i :class="item.icon"></i><span>{{ item.title }}</span></template>
                  <el-menu-item v-for="(child,childIndex) in item.children" :key="childIndex" :index="child.url"><span style="margin-left:10px;">{{child.title}}</span></el-menu-item>
                </el-submenu>
              </template>
            </el-menu>
          </div>
            <div class="aside-foot">
              <el-button :icon="sideIcon" size="mini" circle @click="iconToggle"></el-button>
            </div>
          </el-col>
        </el-row>
      </el-aside>
      <!-- 页面主体 -->
      <el-main style="clear: both;">
        <transition name="move" mode="out-in">
         <!--渲染子页面-->
          <router-view :key="$route.fullPath"></router-view>
        </transition>
      </el-main>
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
        systemActive:"",
        systemOptions:[
          {label: '系统管理',icon:"el-icon-s-tools",mainMenu:[
            {title:"组织架构",icon:"el-icon-office-building",url:"/Organization"},
            {title:"企业管理",icon:"el-icon-school",url:"/EnterpriseManagement"},
            {title:"工厂管理",icon:"el-icon-office-building",url:"/FactoryManagement"},
            {title:"角色权限",icon:"el-icon-s-check",url:"/Role"},
            {title:"班组管理",icon:"el-icon-receiving",url:"/TeamGroup"},
            {title:"人员管理",icon:"el-icon-user",url:"/Personnel"},
            {title:"权限维护",icon:"el-icon-lock",url:"/Permission"},
            {title:"流程管理",icon:"el-icon-share",url:"/flowGraph"},
            {title:"可视化建表",icon:"fa fa-database",url:"/BuildTable"},
            {title:"系统日志",icon:"el-icon-notebook-1",url:"/Log"}
          ]},
        ],
        mainMenuActive:0,
        mainMenu:[], //左侧导航菜单列表
        defaultActiveUrl:"",
        dialogUserVisible:false, //是否弹出个人信息
        userInfo:{},
        isFullScreen:false, //是否全屏
        themeValue:"0",
        themeList:[
          {color:"#ffffff",value:"0"},
          {color:"#1E222B",value:"1"},
          {color:"#0A9168",value:"2"},
        ],
      }
    },
    mounted(){
      if(localStorage.getItem('theme') === "1"){
        this.themeValue = "1"
        $("#app").attr('class','black-theme')
      }else if(localStorage.getItem('theme') === "2"){
        this.themeValue = "2"
        $("#app").attr('class','green-theme')
      }else{
        this.themeValue = "0"
        $("#app").attr('class','white-theme')
      }
    },
    created(){
      window.addEventListener('resize', this.getMenuHeight);
      this.getMenuHeight()
      if(sessionStorage.getItem("LoginStatus")) {
        this.$store.commit('setUser',sessionStorage.getItem('WorkNumber'))
      }else{
        this.$router.push("/login");
      }
      if(this.$route.path === "/home"){ //判断当前路由 设置当前路由对应的菜单
        this.getMainMenu(this.systemOptions[0].mainMenu)
        this.getsystemActive(0)
      }else{
        this.systemOptions.forEach((menu,i) =>{
          if(menu.label === this.$route.meta.type){
            this.mainMenu = menu.mainMenu
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
        },
        deep: true,
      }
    },
    methods:{
      getMenuHeight(){
        if(this.menuIsCollapse){
          this.selfHeight.height = window.innerHeight - 490+'px';
        }else{
          this.selfHeight.height = window.innerHeight - 360+'px';
        }
      },
      getMainMenu(data){ //从子组件选择的系统获取菜单
        this.mainMenu = data
      },
      getsystemActive(data){ //从子组件选择的系统索引
        this.systemActive = data
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
        this.themeValue = value
        localStorage.setItem('theme', value);
        if(value === "0"){
          $("#app").attr('class','white-theme')
        }else if(value === "1"){
          $("#app").attr('class','black-theme')
        }else if(value === "2"){
          $("#app").attr('class','green-theme')
        }
      },

    }
  }
</script>
<style lang="less">

</style>
