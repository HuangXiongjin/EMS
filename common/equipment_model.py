from datetime import datetime

from sqlalchemy import Column, Integer, Unicode, ForeignKey

from common.system_model import Base, engine


class EquipmentTree(Base):
    """设备结构树"""
    __tablename__ = "EquipmentTree"

    ID = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    # 设备编号
    TagCode = Column(Unicode(100), nullable=True)
    # 设备名称
    TagName = Column(Unicode(100), nullable=True)
    # 部门名称
    ChildrenTag = Column(Unicode(100), nullable=True)
    # 车间名称
    ParentTag = Column(Unicode(100), nullable=True)


class Equipment(Base):
    __tablename__ = "Equipment"
    # ID:
    ID = Column(Integer, primary_key=True, autoincrement=True, nullable=True)
    # 设备名称
    EquipmentName = Column(Unicode(128), nullable=True)
    # 设备编号
    EquipmentCode = Column(Unicode(128), nullable=True)
    # 资产编号
    AssetCode = Column(Unicode(128), nullable=True)
    # 出厂编号
    LeaveFactoryCode = Column(Unicode(128), nullable=True)
    # 电子标签码
    ElectronicCode = Column(Unicode(128), nullable=True)
    # 设备类别
    EquipmentType = Column(Unicode(64), nullable=True)
    # 品牌
    Brand = Column(Unicode(64), nullable=True)
    # 规格
    Specs = Column(Unicode(64), nullable=True)
    # 单位
    Unit = Column(Unicode(32), nullable=True)
    # 设备来源
    Source = Column(Unicode(128), nullable=True)
    # 供应商
    Manufacturer = Column(Unicode(128), nullable=True)
    # 设备状态（正常，闲置，维修中，报废）
    Status = Column(Unicode(128), default="正常", nullable=True)
    # 购置时间
    PurchaseTime = Column(Unicode(128), nullable=True, default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    # 购置金额
    PurchaseMoney = Column(Unicode(64), nullable=True)
    # 保修期
    WarrantyTime = Column(Unicode(128), nullable=True, default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    # 投产时间
    UseTime = Column(Unicode(128), nullable=True, default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    # 预计报废时间
    ScrapTime = Column(Unicode(128), nullable=True, default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    # 设备等级（A-关键 B-重要 C-一般）
    Grade = Column(Unicode(64), nullable=True)
    # 负责人
    Director = Column(Unicode(64), nullable=True)
    # 所属部门
    Department = Column(Unicode(128), nullable=True)
    # 放置位置
    Position = Column(Unicode(128), nullable=True)
    # 是否计量设备
    IsCalculate = Column(Unicode(32), nullable=True)
    # 是否折旧设备
    IsDepreciation = Column(Unicode(32), nullable=True)
    # 当前净值
    NetValue = Column(Unicode(64), nullable=True)
    # 技术参数
    TechnicalParameter = Column(Unicode(128), nullable=True)
    # 备注
    Comment = Column(Unicode(32), nullable=True)
    # 设备二维码
    QRCode = Column(Unicode(2048), nullable=True)
    # 设备图片
    Picture = Column(Unicode(5120), nullable=True)


class Allocation(Base):
    """设备调拨"""
    __tablename__ = "Allocation"

    ID = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    # 调拨单号
    No = Column(Unicode(128), nullable=True)
    # 设备名称
    EquipmentName = Column(Unicode(128), nullable=True)
    # 设备编号
    EquipmentCode = Column(Unicode(128), nullable=True)
    # 规格
    Specs = Column(Unicode(64), nullable=True)
    # 调拨部门
    AllocationDepartment = Column(Unicode(128), nullable=True)
    # 调出地点
    AddressOut = Column(Unicode(128), nullable=True)
    # 调入地点
    AddressInto = Column(Unicode(128), nullable=True)
    # 申请时间
    Time = Column(Unicode(64), nullable=True)
    # 申请人
    User = Column(Unicode(64), nullable=True)
    # 调拨原因
    Comment = Column(Unicode(128), nullable=True)
    # 当前节点
    Node = Column(Unicode(64), nullable=True)
    # 当前状态
    Status = Column(Unicode(64), nullable=True)


class Life(Base):
    """操作周期"""
    __tablename__ = "Life"

    ID = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    # 单号
    No = Column(Unicode(128), nullable=True)
    # 操作时间
    Time = Column(Unicode(64), nullable=True)
    # 操作人
    User = Column(Unicode(64), nullable=True)
    # 当前节点
    Node = Column(Unicode(64), nullable=True)
    # 当前状态
    Status = Column(Unicode(64), nullable=True)
    # 操做内容
    Content = Column(Unicode(128), nullable=True)


#
# class InstructionsCenter(Base):
#     """说明书中间表"""
#     __tablename__ = 'InstructionsCenter'
#
#     id = Column(Integer, autoincrement=True, primary_key=True)
#     # 设备/配件编号
#     no = Column(Unicode(32), nullable=False)
#     # 说明书ID
#     instructions = db.relationship("Instructions", backref='InstructionsCenter')
#
#
# class Instructions(Base):
#     """设备/配件说明书"""
#     __tablename__ = 'Instructions'
#
#     id = Column(Integer, autoincrement=True, primary_key=True)
#     # 说明书编号
#     no = Column(Unicode(128), nullable=False)
#     # 说明书类型
#     type = Column(Unicode(32), nullable=False)
#     # 说明书详情
#     detail = Column(Unicode(256), nullable=False)
#     # 中间表id
#     center_id = Column(Integer, ForeignKey('InstructionsCenter.id'))
#
#
# class Fitting(Base):
#     """配件数据"""
#     __tablename__ = 'Fitting'
#
#     id = Column(Integer, autoincrement=True, primary_key=True)
#     # 设备号
#     equipment_no = Column(Unicode(128), nullable=True)
#     # 配件编号
#     fitting_no = Column(Unicode(128), nullable=False)
#     # 配件名称
#     name = Column(Unicode(64), nullable=False)
#     # 配件型号
#     model = Column(Unicode(128), nullable=True)
#     # 配件类型
#     type = Column(Unicode(32), nullable=True)
#     # 使用状态
#     status = Column(Unicode(8), default="未使用")
#     # 生产商
#     manufacturer = Column(Unicode(64), nullable=True)
#     # 进厂日期
#     time = Column(Unicode(32), nullable=True, default=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
#     # 中间表ID
#     # center_id = Column(Integer, primary_key=True)
#
#
# class FittingInto(Base):
#     """配件入库"""
#     __tablename__ = 'FittingInto'
#
#     id = Column(Integer, autoincrement=True, primary_key=True)
#     # 入库单号
#     no = Column(Unicode(256), nullable=False)
#     # 配件编号
#     fitting_no = Column(Unicode(1024), nullable=False)
#     # 配件数量
#     fitting_number = Column(Unicode(256), nullable=False)
#     # 验收状态
#     status = Column(Unicode(8), default="否")
#     # 验收人员
#     worker = Column(Unicode(128), nullable=False)
#     # 入库时间
#     time = Column(Unicode(32), nullable=True, default=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
#
#
# class FittingOut(Base):
#     """配件出库"""
#     __tablename__ = 'FittingOut'
#
#     id = Column(Integer, autoincrement=True, primary_key=True)
#     # 出库单号
#     no = Column(Unicode(256), nullable=False)
#     # 配件编号
#     fitting_no = Column(Unicode(1024), nullable=False)
#     # 配件数量
#     fitting_number = Column(Unicode(256), nullable=False)
#     # 出库人员
#     out_worker = Column(Unicode(128), nullable=False)
#     # 领用人员
#     use_worker = Column(Unicode(128), nullable=False)
#     # 出库时间
#     time = Column(Unicode(32), nullable=True, default=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
#
#
# class Stock(Base):
#     """库存统计"""
#     __tablename__ = 'Stock'
#
#     id = Column(Integer, autoincrement=True, primary_key=True)
#     # 配件型号
#     type = Column(Unicode(64), nullable=False)
#     # 使用数量
#     use_count = Column(Unicode(64), nullable=True)
#     # 剩余数量
#     stock_count = Column(Unicode(64), nullable=True)
#     # 清点人员
#     worker = Column(Unicode(128), nullable=False)
#     # 清点时间
#     time = Column(Unicode(32), nullable=True, default=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
#     # 库存预警
#     status = Column(Unicode(32), default="库存充足")
#
#
# class WorkOrder(Base):
#     """工单记录"""
#     __tablename__ = 'WorkOrder'
#
#     id = Column(Integer, autoincrement=True, primary_key=True)
#     # 工单号
#     no = Column(Unicode(256), nullable=False)
#     # 设备号
#     equipment_no = Column(Unicode(256), nullable=False)
#     # 车间号
#     workshop_no = Column(Unicode(128), nullable=False)
#     # 员工号
#     worker_no = Column(Unicode(128), nullable=False)
#     # 姓名
#     name = Column(Unicode(32), nullable=False)
#     # 工单状态（待处理，待审核，执行中，已完成）
#     status = Column(Unicode(32), default="待处理")
#     # 工单类型（维修，保养，润滑，巡检）
#     type = Column(Unicode(32), nullable=True)
#     # 开始时间
#     start_time = Column(Unicode(32), nullable=True, default=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
#     # 结束时间
#     end_time = Column(Unicode(32), nullable=True, default=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
#
#
# class Scheduling(Base):
#     """排班表"""
#     __tablename__ = 'Scheduling'
#
#     id = Column(Integer, autoincrement=True, primary_key=True)
#     # 设备号
#     equipment_no = Column(Unicode(256), nullable=False)
#     # 车间号
#     workshop_no = Column(Unicode(128), nullable=False)
#     # 工单号
#     no = Column(Unicode(256), nullable=False)
#     # 班组号
#     work_no = Column(Unicode(64), nullable=True)
#     # 班次号
#     work_group = Column(Unicode(64), nullable=True)
#
#
# class FaultRepair(Base):
#     """故障报修"""
#     __tablename__ = 'FaultRepair'
#
#     id = Column(Integer, autoincrement=True, primary_key=True)
#     # 设备号
#     equipment_no = Column(Unicode(256), nullable=False)
#     # 车间号
#     workshop_no = Column(Unicode(128), nullable=False)
#     # 工单号
#     no = Column(Unicode(256), nullable=False)
#     # 员工号
#     worker_no = Column(Unicode(128), nullable=False)
#     # 姓名
#     name = Column(Unicode(32), nullable=False)
#     # 故障原因
#     reason = Column(Unicode(128), nullable=True)
#     # 故障图片
#     picture = Column(Unicode(128), nullable=True)
#     # 申请时间
#     time = Column(Unicode(32), nullable=True, default=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
#
#
# class Record(Base):
#     """保润检记录表"""
#     __tablename__ = "Record"
#
#     id = Column(Integer, autoincrement=True, primary_key=True)
#     # 设备号
#     equipment_no = Column(Unicode(256), nullable=False)
#     # 工单号
#     no = Column(Unicode(256), nullable=False)
#     # 员工号
#     worker_no = Column(Unicode(128), nullable=False)
#     # 姓名
#     name = Column(Unicode(32), nullable=False)
#     # 工单类型（维修，保养，润滑，巡检）
#     type = Column(Unicode(32), nullable=True)
#     # 设备状态（良好,异常）
#     status = Column(Unicode(32), default="良好")
#     # 工作时间
#     time = Column(Unicode(32), nullable=True, default=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
#
#
# class RepairRecord(Base):
#     """维修记录表"""
#     __tablename__ = 'RepairRecord'
#
#     id = Column(Integer, autoincrement=True, primary_key=True)
#     # 设备号
#     equipment_no = Column(Unicode(256), nullable=False)
#     # 工单号
#     no = Column(Unicode(256), nullable=False)
#     # 员工号
#     worker_no = Column(Unicode(128), nullable=False)
#     # 设备状态（良好，异常）
#     status = Column(Unicode(12), default="良好")
#     # 故障原因
#     fault_reason = Column(Unicode(128), nullable=True)
#     # 维修材料
#     repair_material = Column(Unicode(128), nullable=True)
#     # 修复验收(是， 否)
#     repair_status = Column(Unicode(12), default="否")
#     # 故障等级(一级， 二级， 三级)
#     fault_rank = Column(Unicode(12), default="一级")
#     # 维修知识
#     knowledge = Column(Unicode(256), nullable=True)
#     # 工作时间
#     time = Column(Unicode(32), nullable=True, default=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
#
#
# class RepairPlan(Base):
#     """维保检方案"""
#     __tablename__ = 'RepairPlan'
#
#     id = Column(Integer, autoincrement=True, primary_key=True)
#     # 设备号
#     equipment_no = Column(Unicode(256), nullable=False)
#     # 方案编号
#     plan_no = Column(Unicode(128), nullable=False)
#     # 部位
#     position = Column(Unicode(64), nullable=True)
#     # 工具
#     tools = Column(Unicode(64), nullable=True)
#     # 材料
#     material = Column(Unicode(64), nullable=True)
#     # 方法
#     plan = Column(Unicode(64), nullable=True)
#     # 标准
#     standard = Column(Unicode(32), nullable=True)
#     # 周期
#     period = Column(Unicode(32), nullable=True)
#     # 实施部门
#     department = Column(Unicode(32), nullable=True)
#     # 工单类型（维修，保养，巡检）
#     type = Column(Unicode(32), nullable=True)
#
#
# class LubricationPlan(Base):
#     """润滑方案"""
#     __tablename__ = 'LubricationPlan'
#
#     id = Column(Integer, autoincrement=True, primary_key=True)
#     # 设备号
#     equipment_no = Column(Unicode(256), nullable=False)
#     # 方案编号
#     plan_no = Column(Unicode(128), nullable=False)
#     # 润滑部位
#     position = Column(Unicode(64), nullable=True)
#     # 润滑油品
#     oils = Column(Unicode(32), nullable=True)
#     # 润滑方式
#     way = Column(Unicode(32), nullable=True)
#     # 换油数量
#     changes_amount = Column(Unicode(32), nullable=True)
#     # 换油周期
#     oils_changes_period = Column(Unicode(32), nullable=True)
#     # 加油数量
#     add_amount = Column(Unicode(32), nullable=True)
#     # 加油周期
#     oils_add_period = Column(Unicode(32), nullable=True)
#     # 实施部门
#     department = Column(Unicode(32), nullable=True)
#
#
# class OrderVerify(Base):
#     """工单审核"""
#     __tablename__ = 'OrderVerify'
#
#     id = Column(Integer, autoincrement=True, primary_key=True)
#     # 工单号
#     no = Column(Unicode(256), nullable=False)
#     # 审核人
#     name = Column(Unicode(32), nullable=False)
#     # 审核状态（待审核，审核通过）
#     verify_status = Column(Unicode(32), default="待审核")
#     # 审核时间
#     verify_time = Column(Unicode(32), nullable=True, default=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
#     # 计划表
#     # plan = db.relationship("Plan", backref='orderVerify')
#
#
# class Plan(Base):
#     """维保润检计划表"""
#     __tablename__ = 'Plan'
#
#     id = Column(Integer, autoincrement=True, primary_key=True)
#     # 设备号
#     equipment_no = Column(Unicode(256), nullable=False)
#     # 车间号
#     workshop_no = Column(Unicode(128), nullable=False)
#     # 工单号
#     no = Column(Unicode(256), nullable=False)
#     # 创建员工号
#     worker_no = Column(Unicode(128), nullable=False)
#     # 创建人姓名
#     name = Column(Unicode(32), nullable=False)
#     # 工单状态（待处理，待审核，执行中，已完成）
#     no_status = Column(Unicode(32), default="待处理")
#     # 审核状态（待审核，审核通过）
#     verify_status = Column(Unicode(32), default="待审核")
#     # 提醒状态（待提醒，已提醒）
#     remind_status = Column(Unicode(32), default="待提醒")
#     # 工单类型（维修，保养，润滑，巡检）
#     type = Column(Unicode(32), nullable=True)
#     # 预工作时间
#     work_time = Column(Unicode(32), nullable=True, default=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
#     # 创建时间
#     found_time = Column(Unicode(32), nullable=True, default=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
#     # 方案编号
#     plan_no = Column(Unicode(128), nullable=False)
#     # 审核人
#     # verify_id = Column(Integer, ForeignKey('orderVerify.id'))
#
#
# class Task(Base):
#     """任务表"""
#     __tablename__ = 'Task'
#
#     id = Column(Integer, autoincrement=True, primary_key=True)
#     # 设备号
#     equipment_no = Column(Unicode(128), nullable=False)
#     # 车间号
#     workshop_no = Column(Unicode(128), nullable=False)
#     # 工单号
#     no = Column(Unicode(256), nullable=False)
#     # 发放人
#     name = Column(Unicode(32), nullable=False)
#     # 工单状态（待处理，待审核，执行中，已完成）
#     no_status = Column(Unicode(32), default="待处理")
#     # 工单类型（维修，保养，润滑，巡检）
#     type = Column(Unicode(32), nullable=True)
#     # 工时要求
#     work_require = Column(Unicode(32), nullable=True)
#     # 下发时间
#     found_time = Column(Unicode(32), nullable=True, default=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
#
#
# class Monitor(Base):
#     """设备实时监测数据"""
#     __tablename__ = 'Monitor'
#
#     id = Column(Integer, autoincrement=True, primary_key=True)
#     # 设备号
#     equipment_no = Column(Unicode(128), nullable=False)
#     # 当前状态（1：良好 0：异常）
#     status = Column(db.SmallInteger, default=1, nullable=True)
#     # 运行总时间
#     total_time = Column(Unicode(64), nullable=True)
#     # 停机总时间
#     stop_time = Column(Unicode(64), nullable=True)
#     # 维修时间
#     repair_time = Column(Unicode(64), nullable=True)
#     # 故障次数
#     stop_count = Column(Unicode(64), nullable=True)
#
#
# class Kpi(Base):
#     """设备KPI"""
#     __tablename__ = 'Kpi'
#
#     id = Column(Integer, autoincrement=True, primary_key=True)
#     # 设备编号
#     equipment_no = Column(Unicode(128), nullable=False)
#     # 设备完好率
#     whl = Column(Unicode(64), nullable=True)
#     # 设备故障率
#     gzl = Column(Unicode(64), nullable=True)
#     # 维修费用率
#     wxfyl = Column(Unicode(64), nullable=True)
#     # 故障停机率
#     gztjl = Column(Unicode(64), nullable=True)
#     # 维修完成率
#     wxwcl = Column(Unicode(64), nullable=True)
#     # 全局设备率
#     qjsbl = Column(Unicode(64), nullable=True)
#     # 故障发生次数
#     count = Column(Unicode(64), nullable=True)
#


Base.metadata.create_all(engine)
