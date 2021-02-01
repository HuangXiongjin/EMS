from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, Integer, Unicode
from werkzeug.security import generate_password_hash, check_password_hash

from database.connect_db import CONNECT_DATABASE

engine = create_engine(CONNECT_DATABASE)
Session = sessionmaker(bind=engine)
db_session = Session()
Base = declarative_base(engine)


class RunLog(Base):
    __tablename__ = "RunLog"

    ID = Column(Integer, primary_key=True, autoincrement=True, nullable=True)

    # 日期
    OperateTime = Column(Unicode(64), nullable=True)

    # 访问IP
    IP = Column(Unicode(64), nullable=True)

    # 请求路径
    Path = Column(Unicode(64), nullable=True)

    # 请求函数
    Func = Column(Unicode(64), nullable=True)

    # 请求方式
    Method = Column(Unicode(64), nullable=True)

    # 用户
    User = Column(Unicode(64), nullable=True)

    # 响应内容
    Error = Column(Unicode(512), nullable=True)


class CreateTableSet(Base):
    """数据库建表配置"""
    __tablename__ = 'CreateTableSet'

    ID = Column(Integer, primary_key=True, autoincrement=True, nullable=False)

    # 表名:
    TableName = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 表的描述:
    TableDescrip = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)


# # 4.表字段配置：选择一个表，将此表的数据（字段）显示出来（新表只有ID）
class FieldSet(Base):
    """字段表表头"""
    __tablename__ = 'FieldSet'
    # id:
    ID = Column(Integer, primary_key=True, autoincrement=True, nullable=False)

    # 表名称:
    TableName = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # title字段名称（名字）:
    TitleName = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # field字段名（name）:
    FieldName = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # VARCHAR长度:
    length = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 字段类型:
    type = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 字段注释:
    comment = Column(Unicode(65), primary_key=False, autoincrement=False, nullable=True)

    # 是否为主键（默认False）:
    primarykey = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 是否自增（默认False）:
    autoincrement = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 是否为空（默认True）:
    nullable = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 状态:
    Status = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # # isedit是否做添加修改操作（默认否）:
    # Isedit = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # # 列宽:
    # width = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # # edittype输入类型，输入框/下拉框/时间选择框（满足上一条可做编辑操作，默认输入框）:
    # Edittype = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)
    #
    # # downtable下拉框的数据表（满足上一条选择下拉框，选择一个表）:
    # Downtable = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)
    #
    # # sortable该列是否排序,表头显示双箭头(默认false):
    # Sortable = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)
    #
    # # order该列排序方式，满足上条可排序，默认asc( asc/desc):
    # Order = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)
    #
    # # visible该列是否可见(默认true):
    # Visible = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)


class FieldType(Base):
    """表字段类型"""
    __tablename__ = 'FieldType'
    # id:
    ID = Column(Integer, primary_key=True, autoincrement=True, nullable=False)

    # 类型:
    Type = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 描述:
    Description = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)


# 权限表
class Permission(Base):
    __tablename__ = 'Permission'
    # ID
    ID = Column(Integer, primary_key=True, autoincrement=True, nullable=False)

    # 权限名字:
    PermissionName = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 权限类型:
    PermissionType = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 描述:
    Description = Column(Unicode(100), primary_key=False, autoincrement=False, nullable=True)

    # 创建时间
    CreateData = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True,
                        default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


class DepartmentManager(Base):
    """部门"""
    __tablename__ = "DepartmentManager"

    # ID:
    ID = Column(Integer, primary_key=True, autoincrement=True, nullable=False)

    # 部门名称:
    DepartName = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 部门编码:
    DepartCode = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 所属厂区:
    DepartLoad = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)


class Role(Base):
    """角色"""
    __tablename__ = "Role"

    # ID:
    ID = Column(Integer, primary_key=True, autoincrement=True, nullable=False)

    # 角色编码:
    RoleCode = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # RoleName:
    RoleName = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # Description:
    Description = Column(Unicode(50), primary_key=False, autoincrement=False, nullable=True)

    # 所属部门:
    ParentNode = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)


class RoleUser(Base):
    """角色用户表"""
    __tablename__ = 'RoleUser'
    # ID
    ID = Column(Integer, primary_key=True, autoincrement=True, nullable=False)

    # 权限ID:
    UserID = Column(Integer, primary_key=False, autoincrement=False, nullable=True)

    # 权限名字:
    UserName = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 角色ID:
    RoleID = Column(Integer, primary_key=False, autoincrement=False, nullable=True)

    # 角色名称:
    RoleName = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 创建时间
    CreateDate = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True,
                        default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


class RolePermission(Base):
    """角色默认权限表"""
    __tablename__ = 'RolePermission'
    # ID
    ID = Column(Integer, primary_key=True, autoincrement=True, nullable=False)

    # 角色ID:
    RoleID = Column(Integer, primary_key=False, autoincrement=False, nullable=True)

    # 角色名称:
    RoleName = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 权限ID:
    PermissionID = Column(Integer, primary_key=False, autoincrement=False, nullable=True)

    # 权限名字:
    PermissionName = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 创建时间
    CreateDate = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True,
                        default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


class ModulMenus(Base):
    """模块菜单表"""
    __tablename__ = 'ModulMenus'
    # 模块ID
    ID = Column(Integer, primary_key=True, autoincrement=True)

    # 模块菜单名字:
    ModulMenuName = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 模块菜单编码:
    ModulMenuCode = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 菜单路由:
    ModulMenuRoute = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 创建时间
    CreateDate = Column(Unicode(32), default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), nullable=True)

    # 父节点
    ParentNode = Column(Integer, primary_key=False, autoincrement=False, nullable=True)

    # 菜单类型:
    MenuType = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 菜单图标:
    MenuLogo = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 菜单创建人:
    Creator = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)


# 用户班组表
class UserShiftsGroup(Base):
    __tablename__ = 'UserShiftsGroup'
    # ID
    ID = Column(Integer, primary_key=True, autoincrement=True, nullable=False)

    # 用户ID:
    UserID = Column(Integer, primary_key=False, autoincrement=False, nullable=True)

    # 用户名:
    Name = Column(Unicode(64), primary_key=False, autoincrement=False, nullable=True)

    # 班组ID:
    ShiftsGroupID = Column(Integer, primary_key=False, autoincrement=False, nullable=True)

    # 班组名称
    ShiftsGroupName = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 创建时间
    CreateDate = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True,
                        default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


class User(Base):
    __tablename__ = "User"

    ID = Column(Integer, primary_key=True, autoincrement=True, nullable=False)

    # 用户名:
    Name = Column(Unicode(64), nullable=True)

    # 密码:
    Password = Column(Unicode(150), nullable=True)

    # 工号:
    WorkNumber = Column(Unicode(32), nullable=True)

    # 所属岗位:
    StationName = Column(Unicode(65), nullable=True)

    # 登录状态:
    Status = Column(Unicode(32), nullable=True)

    # session_id:
    session_id = Column(Unicode(32), nullable=True)

    # 所属部门:
    OrganizationName = Column(Unicode(50), nullable=True)

    # 所属厂区:
    FactoryName = Column(Unicode(65), nullable=True)

    # 班组类型
    ShiftsGroupType = Column(Unicode(32), nullable=True)

    # 上次登录时间:
    LastLoginTime = Column(Unicode(32), nullable=True)

    # 创建时间:
    CreateTime = Column(Unicode(32), nullable=True)

    # 创建用户:
    Creater = Column(Unicode(65), nullable=True)

    # 是否锁定:
    IsLock = Column(Unicode(32), nullable=True)

    def password(self, password):
        self.Password = generate_password_hash(password)
        return self.Password

    # 定义验证密码的函数confirm_password
    def confirm_password(self, password):
        return check_password_hash(self.Password, password)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.ID)


class ShiftsGroup(Base):
    __tablename__ = "ShiftsGroup"
    # ID:
    ID = Column(Integer, primary_key=True, autoincrement=True, nullable=True)
    # 班组编码
    ShiftsGroupCode = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)
    # 班组名称
    ShiftsGroupName = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)
    # 班组类型
    ShiftsGroupType = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)
    # 描述:
    Description = Column(Unicode(100), primary_key=False, autoincrement=False, nullable=True)
    # 创建日期:
    CreateDate = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)


class WorkShop(Base):
    """车间"""
    __tablename__ = "WorkShop"

    # ID:
    ID = Column(Integer, primary_key=True, autoincrement=True, nullable=False)

    # 车间名称:
    WorkShopName = Column(Unicode(52), primary_key=False, autoincrement=False, nullable=True)

    # 车间编码:
    WorkShopCode = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 所属厂区:
    FactoryName = Column(Unicode(52), primary_key=False, autoincrement=False, nullable=True)

    # 描述:
    Description = Column(Unicode(100), primary_key=False, autoincrement=False, nullable=True)


class AreaMaintain(Base):
    """厂区"""
    __tablename__ = "AreaMaintain"

    # ID:
    ID = Column(Integer, primary_key=True, autoincrement=True, nullable=False)

    # 区域编码:
    AreaCode = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 区域名称:
    AreaName = Column(Unicode(65), primary_key=False, autoincrement=False, nullable=True)

    # 所属厂区:
    FactoryName = Column(Unicode(65), primary_key=False, autoincrement=False, nullable=True)


# class Factory(Base):
#     __tablename__ = "Factory"
#
#     # ID:
#     ID = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
#
#     # 所属企业:
#     EnterpriseName = Column(Unicode(65), primary_key=False, autoincrement=False, nullable=True)
#
#     # 厂名:
#     FactoryName = Column(Unicode(65), primary_key=False, autoincrement=False, nullable=True)
#
#     # 所在地区:
#     Region = Column(Unicode(65), primary_key=False, autoincrement=False, nullable=True)


# class Station(Base):
#     '''岗位'''
#     __tablename__ = "Station"
#
#     # ID:
#     ID = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
#
#     # 地址:
#     Address = Column(Unicode(65), primary_key=False, autoincrement=False, nullable=True)
#
#     # 电话:
#     Phone = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)
#
#     # 岗位负责人:
#     PersonCharge = Column(Unicode(65), primary_key=False, autoincrement=False, nullable=True)
#
#     # 岗位职责:
#     Responsibility = Column(Unicode(100), primary_key=False, autoincrement=False, nullable=True)
#
#     # 所属部门:
#     DepartName = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)
#
#     # 岗位类型:
#     StationType = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)
#
#     # 岗位名称:
#     StationName = Column(Unicode(65), primary_key=False, autoincrement=False, nullable=True)
#
#     # 岗位编码:
#     StationCode = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)
#
#
#
# class Enterprise(Base):
#     __tablename__ = "Enterprise"
#
#     # ID:
#     ID = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
#
#     # 上级企业:
#     ParentNode = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)
#
#     # 企业类型:
#     Type = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)
#
#     # 描述:
#     Description = Column(Unicode(65), primary_key=False, autoincrement=False, nullable=True)
#
#     # 父节点名称:
#     ParentNodeName = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)
#
#     # 企业代码:
#     EnterpriseNo = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)
#
#     # 企业名称:
#     EnterpriseName = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)
#
#     # 企业编码:
#     EnterpriseCode = Column(Unicode(65), primary_key=False, autoincrement=False, nullable=True)
#
#
# class MenuType(Base):
#     __tablename__ = "MenuType"
#
#     # ID:
#     ID = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
#
#     # 类型名称:
#     TypeName = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)
#
#     # 类型编码:
#     TypeCode = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)
#
#
# class plantCalendarScheduling(Base):
#     '''日历'''
#     __tablename__ = "plantCalendarScheduling"
#
#     # ID:
#     ID = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
#
#     # 颜色:
#     color = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)
#
#     # 标题:
#     title = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)
#
#     # 时间:
#     start = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)
#
#     # 结束:
#     end = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)
#
#
class TechnologicalProcess(Base):
    '''流程'''
    __tablename__ = "TechnologicalProcess"

    # ID:
    ID = Column(Integer, primary_key=True, autoincrement=True, nullable=False)

    # 流程名:
    ProcessName = Column(Unicode(80), primary_key=False, autoincrement=False, nullable=True)

    # 流程结构:
    ProcessStructure = Column(Unicode(MAX), primary_key=False, autoincrement=False, nullable=True)

    # 流程结构:
    Icon = Column(Unicode(50), primary_key=False, autoincrement=False, nullable=True)

    # 注释:
    Describtion = Column(Unicode(100), primary_key=False, autoincrement=False, nullable=True)

    # 录入时间:
    InputDate = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)
#
#
# # 模块菜单表
# class ModulMenus(Base):
#     __tablename__ = 'ModulMenus'
#     # 模块ID
#     ID = Column(Integer, primary_key=True, autoincrement=True)
#
#     # 模块菜单名字:
#     ModulMenuName = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)
#
#     # 模块菜单编码:
#     ModulMenuCode = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)
#
#     # 菜单路由:
#     ModulMenuRoute = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)
#
#     # 创建时间
#     CreateDate = Column(Unicode(32), default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), nullable=True)
#
#     # 父节点
#     ParentNode = Column(Integer, primary_key=False, autoincrement=False, nullable=True)
#
#     # 菜单类型:
#     MenuType = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)
#
#     # 菜单图标:
#     MenuLogo = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)
#
#     # 菜单创建人:
#     Creator = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)
#
#
# # 流程存储
# class ProcessStorage(Base):
#     '''流程存储'''
#     __tablename__ = 'ProcessStorage'
#     # 模块ID
#     ID = Column(Integer, primary_key=True, autoincrement=True)
#
#     # 流程存储名:
#     ProcessName = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)
#
#     # 流程存储code:
#     ModulMenuCode = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)
#
#     # 流程存储内容:
#     ModulMenuRoute = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)
#
#     # 存储时间
#     CreateDate = Column(Unicode(32), default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), nullable=True)
#
#
# # 首页模块存储
# class HomeModule(Base):
#     '''首页模块存储'''
#     __tablename__ = 'HomeModule'
#     # 模块ID
#     ID = Column(Integer, primary_key=True, autoincrement=True)
#
#     # 模块名称:
#     HomeModuleName = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)
#
#     # 模块内容:
#     HomeModuleContent = Column(Unicode(500), primary_key=False, autoincrement=False, nullable=True)
#
#     # 描述:
#     Description = Column(Unicode(100), primary_key=False, autoincrement=False, nullable=True)
#
#     # 存储时间
#     CreateDate = Column(Unicode(32), default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), nullable=True)


# 生成表单的执行语句
Base.metadata.create_all(engine)
