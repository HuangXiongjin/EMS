from datetime import datetime

from sqlalchemy import Column, Integer, Unicode

from common.system_model import Base, engine

#
# class KeepRecord(Base):
#     """保养记录"""
#     __tablename__ = 'KeepRecord'
#
#     ID = Column(Integer, autoincrement=True, primary_key=True)
#     # 工单号
#     No = Column(Unicode(256), nullable=False)
#     # 设备号
#     EquipmentCode = Column(Unicode(256), nullable=True)
#     # 姓名
#     Name = Column(Unicode(32), nullable=True)
#     # 保养材料
#     Material = Column(Unicode(512), nullable=True)
#     # 保养项目
#     KeepProject = Column(Unicode(1024), nullable=True)
#     # 开始时间
#     StartTime = Column(Unicode(32), nullable=True, default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
#     # 结束时间
#     EndTime = Column(Unicode(32), nullable=True, default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


class KeepPlan(Base):
    """保养计划"""
    __tablename__ = 'KeepPlan'

    ID = Column(Integer, autoincrement=True, primary_key=True)
    # 计划单号
    No = Column(Unicode(256), nullable=False)
    # 流程ID
    TID = Column(Integer, nullable=True)
    # 设备号
    EquipmentCode = Column(Unicode(256), nullable=True)
    # 保养设备
    KeepEquipment = Column(Unicode(1024), nullable=True)
    # 计划名称
    PlanName = Column(Unicode(128), nullable=True)
    # 关联保养标准单号
    KeepStandardNo = Column(Unicode(256), nullable=True)
    # 制定人
    PlanUser = Column(Unicode(128), nullable=True)
    # 保养类型（单次保养，周期保养）
    Type = Column(Unicode(128), nullable=True)
    # 保养周期
    Circle = Column(Unicode(128), nullable=True)
    # 保养项目
    KeepProject = Column(Unicode(1024), nullable=True)
    # 提醒时间(单位：天)
    WarningTime = Column(Unicode(64), nullable=True)
    # 创建时间
    FoundTime = Column(Unicode(128), nullable=True)
    # 下次保养时间
    NextKeepTime = Column(Unicode(128), nullable=True)
    # 当前节点
    Node = Column(Unicode(64), nullable=True)
    # 当前状态
    Status = Column(Unicode(64), nullable=True)
    # 接收人
    Receiver = Column(Unicode(64), nullable=True)
    # 工单状态（待接单-已接单-已完成）
    WorkStatus = Column(Unicode(64), nullable=True)
    # 开始时间
    StartTime = Column(Unicode(32), nullable=True, default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    # 结束时间
    EndTime = Column(Unicode(32), nullable=True, default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    # 备注
    Comment = Column(Unicode(128), nullable=True)


class FaultRepair(Base):
    """故障报修"""
    __tablename__ = 'FaultRepair'

    ID = Column(Integer, autoincrement=True, primary_key=True)
    # 报修单号
    No = Column(Unicode(256), nullable=False)
    # 设备号
    EquipmentCode = Column(Unicode(256), nullable=False)
    # 设备位置
    Position = Column(Unicode(128), nullable=True)
    # 设备状态（正常，带病运行，维修中，报废）
    EquipmentStatus = Column(Unicode(128), nullable=True, default='带病运行')
    # 报修人
    Name = Column(Unicode(32), nullable=False)
    # 故障类型(电气故障-气动故障-机械故障-管道故障)
    FaultType = Column(Unicode(32), nullable=False)
    # 故障等级(一般-严重-紧急)
    FaultLevel = Column(Unicode(64), nullable=True)
    # 故障描述
    FaultComment = Column(Unicode(128), nullable=True)
    # 故障原因（违规操作-磨损老化）
    Reason = Column(Unicode(128), nullable=True)
    # 故障图片
    Picture = Column(Unicode(128), nullable=True)
    # 报修时间
    Time = Column(Unicode(32), nullable=True, default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


class EquipmentScrap(Base):
    """设备报废"""
    __tablename__ = 'EquipmentScrap'

    ID = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    # 报废单号
    No = Column(Unicode(128), nullable=True)
    # 设备名称
    EquipmentName = Column(Unicode(128), nullable=True)
    # 设备编号
    EquipmentCode = Column(Unicode(128), nullable=True)
    # 报废申请时间
    ApplyTime = Column(Unicode(64), nullable=True)
    # 报废时间
    ScrapTime = Column(Unicode(64), nullable=True)
    # 申请人
    User = Column(Unicode(64), nullable=True)
    # 报废原因
    Comment = Column(Unicode(128), nullable=True)
    # 当前节点
    Node = Column(Unicode(64), nullable=True)
    # 当前状态
    Status = Column(Unicode(64), nullable=True)


class WBJStandard(Base):
    """维保检标准"""
    __tablename__ = 'WBJStandard'

    ID = Column(Integer, autoincrement=True, primary_key=True)
    # 标准编号
    StandardNo = Column(Unicode(128), nullable=False)
    # 标准名称
    StandardName = Column(Unicode(128), nullable=False)
    # 标准要求
    Standard = Column(Unicode(32), nullable=True)
    # 适用设备类别
    EquipmentType = Column(Unicode(256), nullable=False)
    # 作业内容
    WorkContent = Column(Unicode(128), nullable=True)
    # 工具
    Tools = Column(Unicode(64), nullable=True)
    # 材料
    Material = Column(Unicode(64), nullable=True)
    # 方法
    Plan = Column(Unicode(64), nullable=True)
    # 质量要求
    QualityRequirement = Column(Unicode(128), nullable=True)
    # 实施部门
    Department = Column(Unicode(32), nullable=True)
    # 工单类型（维修，保养，巡检）
    Type = Column(Unicode(32), nullable=True)


class LubricationScheme(Base):
    """润滑标准"""
    __tablename__ = 'LubricationScheme'

    ID = Column(Integer, autoincrement=True, primary_key=True)
    # 适用设备类别
    EquipmentType = Column(Unicode(256), nullable=False)
    # 方案编号
    SchemeNo = Column(Unicode(128), nullable=False)
    # 润滑部位
    Position = Column(Unicode(64), nullable=True)
    # 润滑油品
    Oils = Column(Unicode(32), nullable=True)
    # 润滑方式
    Way = Column(Unicode(32), nullable=True)
    # 换油数量
    Changes_amount = Column(Unicode(32), nullable=True)
    # 换油周期
    OilsChangesPeriod = Column(Unicode(32), nullable=True)
    # 加油数量
    AddAmount = Column(Unicode(32), nullable=True)
    # 加油周期
    OilsAddPeriod = Column(Unicode(32), nullable=True)
    # 实施部门
    Department = Column(Unicode(32), nullable=True)


# class StandardEquipment(Base):
#     """标准适用设备列表"""
#


class BRJRecord(Base):
    """保润检记录表"""
    __tablename__ = "BRJRecord"

    ID = Column(Integer, autoincrement=True, primary_key=True)
    # 工单号
    No = Column(Unicode(256), nullable=False)
    # 设备编号
    EquipmentCode = Column(Unicode(256), nullable=False)
    # 姓名
    WorkName = Column(Unicode(32), nullable=False)
    # 工单类型（维修，保养，润滑，巡检）
    Type = Column(Unicode(32), nullable=True)
    # 设备状态（良好,异常）
    Status = Column(Unicode(32), default="良好")
    # 是否已经报修
    ISRepair = Column(Unicode(32), default="已报修")
    # 工作时间
    Time = Column(Unicode(32), nullable=True, default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


class RepairRecord(Base):
    """维修记录表"""
    __tablename__ = 'RepairRecord'

    ID = Column(Integer, autoincrement=True, primary_key=True)
    # 工单号
    No = Column(Unicode(256), nullable=True)
    # 设备编号
    EquipmentCode = Column(Unicode(256), nullable=True)
    # 设备名称
    EquipmentName = Column(Unicode(128), nullable=True)
    # 报障人
    FaultName = Column(Unicode(64), nullable=True)
    # 报障时间
    FaultTime = Column(Unicode(32), nullable=True, default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    # 设备状态（带病运行，正常，故障）
    EquipmentStatus = Column(Unicode(12), default="正常")
    # 工单状态（已分派-已验收-已撤销-维修中-带分派）
    WorkStatus = Column(Unicode(64), nullable=True)
    # 维修员工
    WorkerName = Column(Unicode(128), nullable=True)
    # 验收人
    CheckName = Column(Unicode(64), nullable=True)
    # 验收时间
    CheckTime = Column(Unicode(32), nullable=True, default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    # 故障原因
    FaultReason = Column(Unicode(128), nullable=True)
    # 故障类型（管道故障-机械故障-电气故障）
    FaultType = Column(Unicode(128), nullable=True)
    # 故障等级(一般-严重-紧急)
    FaultLevel = Column(Unicode(64), nullable=True)
    # 故障描述
    FaultComment = Column(Unicode(128), nullable=True)
    # 维修材料
    RepairMaterial = Column(Unicode(128), nullable=True)
    # 维修知识/解决方法
    Knowledge = Column(Unicode(256), nullable=True)


Base.metadata.create_all(engine)
