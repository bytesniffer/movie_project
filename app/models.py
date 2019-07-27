# _*_ coding: utf-8 _*_
__author__ = 'mtianyan'
__date__ = '2017/8/26 17:05'

from datetime import datetime
from app import db


# 会员数据模型
class User(db.Model):
    __tablename__ = "user"
    __table_args__ = {"useexisting": True}
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(100), unique=True)  # 昵称
    pwd = db.Column(db.String(100))  # 密码
    email = db.Column(db.String(100), unique=True)  # 邮箱
    phone = db.Column(db.String(11), unique=True)  # 手机号
    info = db.Column(db.Text)  # 个性简介
    face = db.Column(db.String(255))  # 头像

    # addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 注册时间
    uuid = db.Column(db.String(255), unique=True)  # 唯一标识符
    create_time = db.Column(db.DateTime, index=False, default=datetime.now)  # create time
    update_time = db.Column(db.DateTime, index=False, default=datetime.now)  # create time
    status = db.Column(db.INT, index=False, default=0)
    # （下面是设置外键的第二步,指向Userlog模型，进行一个互相关系的绑定）
    userlogs = db.relationship('Userlog', backref='user')  # 会员日志外键关系关联
    comments = db.relationship('Comment', backref='user')  # 评论外键关系关联
    moviecols = db.relationship('Moviecol', backref='user')  # 收藏外键关系关联

    def __repr__(self):
        return '<User %r>' % self.name

    def check_pwd(self, pwd):
        from werkzeug.security import check_password_hash
        return check_password_hash(self.pwd, pwd)


# 会员登录日志
class Userlog(db.Model):
    __tablename__ = "user_log"
    __table_args__ = {"useexisting": True}
    id = db.Column(db.Integer, primary_key=True)  # 编号
    # （下面是设置外键的第一步）:指向user表的id字段
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # 所属会员
    ip = db.Column(db.String(100))  # ip地址
    create_time = db.Column(db.DateTime, index=False)  # create time
    update_time = db.Column(db.DateTime, index=False, default=datetime.now)  # create time
    status = db.Column(db.INT, index=False, default=0)

    def __repr__(self):
        return '<User %r>' % self.id


# type
class Movietype(db.Model):
    __tablename__ = "movie_type"
    __table_args__ = {"useexisting": True}
    id = db.Column(db.CHAR(4), primary_key=True)  # 编号
    name = db.Column(db.String(100))  # 标题
    en = db.Column(db.String(100))
    sort = db.Column(db.SMALLINT)
    group_id = db.Column(db.CHAR(2))
    create_time = db.Column(db.DateTime, index=False)  # create time
    update_time = db.Column(db.DateTime, index=False, default=datetime.now)  # create time
    status = db.Column(db.INT, index=False, default=0)
    #addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 添加电影时间
    # （设置外键的第二步）关联模型，相互关系
    movies = db.relationship("Movie", backref='tag')  # 电影外键关系关联

    def __repr__(self):
        return "<Movie type %r>" % self.name


# config
class Config(db.Model):
    __tablename__ = "config"
    __table_args__ = {"useexisting": True}
    id = db.Column(db.CHAR(8), primary_key=True)  # 编号
    name = db.Column(db.String(100), unique=True)  # 标题
    sort = db.Column(db.SMALLINT)
    group_id = db.Column(db.CHAR(5))
    remark = db.Column(db.String(15), comment='remark')
    create_time = db.Column(db.DateTime, index=False)  # create time
    update_time = db.Column(db.DateTime, index=False, default=datetime.now)  # create time
    status = db.Column(db.INT, index=False, default=0)

    def __repr__(self):
        return "<Config %r>" % self.name

# 电影
class Movie(db.Model):
    __tablename__ = "movie"
    __table_args__ = {"useexisting": True}
    id = db.Column(db.Integer, primary_key=True)  # 编号
    title = db.Column(db.String(255))  # 标题
    total_episode = db.Column(db.INT, comment='total episode')
    update_episode = db.Column(db.INT, comment='updated episode')
    url = db.Column(db.String(255))  # 地址
    year = db.Column(db.INT)
    poster = db.Column(db.String(255))  # 封面
    actors = db.Column(db.String(100))
    director = db.Column(db.String(45))
    writer = db.Column(db.String(45))
    info = db.Column(db.Text)  # 电影简介
    #  （设置外键第一步）
    type_id = db.Column(db.CHAR(4), db.ForeignKey('movie_type.id'))  # 所属类型
    type_group_id = db.Column(db.CHAR(2), nullable=False)  # 所属标签
    note = db.Column(db.String(15), comment='quality of movie')
    star = db.Column(db.SmallInteger, default=0)  # 星级
    playnum = db.Column(db.BigInteger, default=0)  # 播放量
    commentnum = db.Column(db.BigInteger, default=0)  # 评论量
    language = db.Column(db.String(25))
    source = db.Column(db.String(15), comment='resource provider code')
    source_id = db.Column(db.INT, comment='original resource id on provider side')
    area = db.Column(db.String(255))  # 上映地区
    length = db.Column(db.String(100))  # 播放时间
    release_time = db.Column(db.Date)  # 上映时间
    create_time = db.Column(db.DateTime, index=False)  # create time
    update_time = db.Column(db.DateTime, index=False, default=datetime.now)  # create time
    status = db.Column(db.INT, index=False, default=0)
    comments = db.relationship("Comment", backref='movie')  # 评论外键关系关联
    moviecols = db.relationship("Moviecol", backref='movie')  # 收藏外键关系关联

    def __repr__(self):
        return "<Movie %r>" % self.title

    def name(self, elem):
        return elem['name']

    def play_list(self):
        plays = []
        if self.url:
            for v in self.url.split('#'):
                record = v.split('$')
                play = {}
                if len(record) > 1:
                    play['name'] = record[0]
                    play['url'] = record[1]
                if play is not None:
                    plays.append(play)
        plays.sort(key=self.name)
        return plays


# 上映预告
class Preview(db.Model):
    __tablename__ = "preview"
    __table_args__ = {"useexisting": True}
    id = db.Column(db.Integer, primary_key=True)  # 编号
    title = db.Column(db.String(255), unique=True)  # 标题
    poster = db.Column(db.String(255), unique=True)  # 封面
    actors = db.Column(db.String(100))
    remark = db.Column(db.String(45), comment='quality of movie')
    total_episode = db.Column(db.INT, comment='total episode')
    update_episode = db.Column(db.INT, comment='updated episode')
    type_id = db.Column(db.CHAR(4), db.ForeignKey('movie_type.id'))  # 所属类型
    type_group_id = db.Column(db.CHAR(2), nullable=False)  # 所属标签
    create_time = db.Column(db.DateTime, index=False)  # create time
    update_time = db.Column(db.DateTime, index=False, default=datetime.now)  # create time
    status = db.Column(db.INT, index=False, default=0)

    def __repr__(self):
        return "<Preview %r>" % self.title


# 评论
class Comment(db.Model):
    __tablename__ = "comment"
    __table_args__ = {"useexisting": True}
    id = db.Column(db.Integer, primary_key=True)  # 编号
    content = db.Column(db.Text)  # 评论内容
    create_time = db.Column(db.DateTime, index=False, default=datetime.now)  # create time
    update_time = db.Column(db.DateTime, index=False, default=datetime.now)  # create time
    status = db.Column(db.INT, index=False, default=0)
    # 关联外键第一步，还要去user表和movie表进行第二步
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))  # 所属电影
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # 所属用户
    # addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 添加时间

    def __repr__(self):
        return "<Comment %r>" % self.id


# 电影收藏
class Moviecol(db.Model):
    __tablename__ = "movie_collection"
    __table_args__ = {"useexisting": True}
    id = db.Column(db.Integer, primary_key=True)  # 编号
    # 关联外键第一步，还要去user表和movie表进行第二步
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))  # 所属电影
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # 所属用户
    create_time = db.Column(db.DateTime, index=False, default=datetime.now)  # create time
    update_time = db.Column(db.DateTime, index=False, default=datetime.now)  # create time
    status = db.Column(db.INT, index=False, default=0)

    def __repr__(self):
        return "<Moviecol %r>" % self.id


# 权限
class Auth(db.Model):
    __tablename__ = "auth"
    __table_args__ = {"useexisting": True}
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(100), unique=True)  # 名称
    url = db.Column(db.String(255), unique=True)  # 地址
    create_time = db.Column(db.DateTime, index=False, default=datetime.now)  # create time
    update_time = db.Column(db.DateTime, index=False, default=datetime.now)  # create time
    status = db.Column(db.INT, index=False, default=0)

    def __repr__(self):
        return "<Auth %r>" % self.name


# 角色
class Role(db.Model):
    __tablename__ = "role"
    __table_args__ = {"useexisting": True}
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(100), unique=True)  # 名称
    auths = db.Column(db.String(600))  #
    create_time = db.Column(db.DateTime, index=False, default=datetime.now)  # create time
    update_time = db.Column(db.DateTime, index=False, default=datetime.now)  # create time
    status = db.Column(db.INT, index=False, default=0)
    admins = db.relationship("Admin", backref='role')  # 管理员外键关系关联

    def __repr__(self):
        return "<Role %r>" % self.name


# 管理员
class Admin(db.Model):
    __tablename__ = "admin"
    __table_args__ = {"useexisting": True}
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(100), unique=True)  # 管理员账号
    pwd = db.Column(db.String(100))  # 管理员密码
    is_super = db.Column(db.SmallInteger)  # 是否为超级管理员，0为超级管理员
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))  # 所属角色
    create_time = db.Column(db.DateTime, index=False, default=datetime.now)  # create time
    update_time = db.Column(db.DateTime, index=False, default=datetime.now)  # create time
    status = db.Column(db.INT, index=False, default=0)
    # addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 添加时间
    adminlogs = db.relationship("Adminlog", backref='admin')  # 管理员登录日志外键关系关联
    oplogs = db.relationship("Oplog", backref='admin')  # 管理员操作日志外键关系关联

    def __repr__(self):
        return "<Admin %r>" % self.name

    def check_pwd(self, pwd):
        from werkzeug.security import check_password_hash
        return check_password_hash(self.pwd, pwd)


# 管理员登录日志
class Adminlog(db.Model):
    __tablename__ = "admin_log"
    __table_args__ = {"useexisting": True}
    id = db.Column(db.Integer, primary_key=True)  # 编号
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'))  # 所属管理员
    ip = db.Column(db.String(100))  # 登录IP
    create_time = db.Column(db.DateTime, index=False, default=None)  # create time
    update_time = db.Column(db.DateTime, index=False, default=datetime.now)  # create time
    status = db.Column(db.INT, index=False, default=0)

    def __repr__(self):
        return "<Adminlog %r>" % self.id


class Search(db.Model):
    __tablename__ = 'searches'
    __table_args_ = {"useexisting": True}
    id = db.Column(db.Integer, primary_key=True)  # 编号
    key = db.Column(db.String(100))  # search key
    total = db.Column(db.INT)  # result count
    create_time = db.Column(db.DateTime, index=False, default=None)  # create time
    status = db.Column(db.INT, index=False, default=0)

    def __repr__(self):
        return "<Search %r>" % self.id


# 操作日志
class Oplog(db.Model):
    __tablename__ = "op_log"
    __table_args__ = {"useexisting": True}
    id = db.Column(db.Integer, primary_key=True)  # 编号
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'))  # 所属管理员
    ip = db.Column(db.String(100))  # 操作IP
    reason = db.Column(db.String(600))  # 操作原因
    create_time = db.Column(db.DateTime, index=False, default=datetime.now)  # create time
    update_time = db.Column(db.DateTime, index=False, default=datetime.now)  # create time
    status = db.Column(db.INT, index=False, default=0)

    def __repr__(self):
        return "<Oplog %r>" % self.id

