#  -*- coding: utf-8 -*-
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String, Float, Date
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import create_engine
from sqlalchemy import or_, and_
from sqlalchemy.orm import sessionmaker
import cx_Oracle
from datetime import datetime, timedelta
import re
from sys import stdout
from random import randint
import logging
from logging.config import dictConfig
from edu_logconfig import LOGCONFIG


dictConfig(LOGCONFIG)
LOG = logging.getLogger('edu_dbclient')

DB_CODE = 'cp1251'


def get_single_query_result(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        if len(res) != 1 or len(res[0]) != 1:
            raise Exception('Error: database returned '
                            'non single result - {}'.format(res))
        return res[0][0]
    return wrapper


def get_first_query_result_if_any(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        if len(res) == 0 or len(res[0]) == 0:
            return None
        else:
            return res[0][0]
    return wrapper


def show_multi_data(headline, data, filename=None):
    line_format = '{}\n'
    if filename:
        with open(str(filename), 'a+') as outfile:
            outfile.write(line_format.format(headline))
            for each in data:
                outfile.write(line_format.format(each))
    else:
        print line_format.format(headline),
        for each in data:
            print line_format.format(each),


class DBClient(object):
    Base = declarative_base()

    EduObjectType = {'Student': 1, 'Course': 2, 'Contract': 3}

    class EduObjectStatus(Base):
        __tablename__ = 'edu_object_status'

        object_status_id = Column(Integer, primary_key=True)
        status_name = Column(String)
        object_type_id = Column(Integer)

        def __repr__(self):
            res = u'<EduObjectStatus(object_status_id={}, ' \
                  u'status_name={})>'.format(
                    self.object_status_id,
                    str(self.status_name).decode(DB_CODE)
            )
            return res.encode(stdout.encoding, errors='replace')

    class EduObject(Base):
        __tablename__ = 'edu_object'

        object_id = Column(Integer, primary_key=True)
        object_name = Column(String)
        object_type_id = Column(Integer)
        object_status_id = Column(Integer)
        reference = Column(String)

        def __repr__(self):
            res = u'<EduObject(object_id={}, object_name={}, ' \
                  u'reference={})>'.format(
                    self.object_id, str(self.object_name).decode(DB_CODE),
                    self.reference
            )
            return res.encode(stdout.encoding, errors='replace')

    class EduCourse(Base):
        __tablename__ = 'edu_course'

        object_id = Column(Integer,
                           ForeignKey('edu_object.object_id'),
                           primary_key=True)
        course_duration = Column(Integer)
        course_cost = Column(Float)

        def __repr__(self):
            res = u'<EduCourse(object_id={}, course_duration={}, ' \
                  u'course_cost={})>'.format(
                    self.object_id, self.course_duration, self.course_cost
            )
            return res.encode(stdout.encoding, errors='replace')

    class EduStudent(Base):
        __tablename__ = 'edu_student'

        object_id = Column(Integer,
                           ForeignKey('edu_object.object_id'),
                           primary_key=True)
        last_name = Column(String)
        first_name = Column(String)
        second_name = Column(String)
        home_phone = Column(String)
        mobile_phone = Column(String)
        work_phone = Column(String)
        e_mail = Column(String)

        def __repr__(self):
            res = u'<EduStudent(object_id={}, name={} {} {})>'.format(
                self.object_id,
                str(self.last_name).decode(DB_CODE),
                str(self.first_name).decode(DB_CODE),
                str(self.second_name).decode(DB_CODE)
            )
            return res.encode(stdout.encoding, errors='replace')

    class EduContract(Base):
        __tablename__ = 'edu_contract'

        object_id = Column(Integer, primary_key=True)
        student_id = Column(Integer,
                            ForeignKey('edu_student.object_id'))
        course_id = Column(Integer,
                           ForeignKey('edu_course.object_id'))
        begin_date = Column(Date)
        creation_date = Column(Date)
        end_date = Column(Date)
        contract_number = Column(String)
        cost = Column(Float)

        def __repr__(self):
            res = u'<EduContract(object_id={}, student_id={}, ' \
                  u'course_id={}, contract_num={})>'.format(
                    self.object_id, self.student_id, self.course_id,
                    str(self.contract_number).decode(DB_CODE)
            )
            return res.encode(stdout.encoding, errors='replace')

    def __init__(self, dbtype='sqlite', dbname='/tmp.db',
                 username=None, password=None):
        self.dbtype = dbtype
        self.engine = self.get_engine(dbtype, dbname, username, password)
        self.session = self.open_session(self.engine)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close_session(self.session)

    @staticmethod
    def get_engine(dbtype, dbname, username=None, password=None):
        engine = None
        try:
            if username:
                cstr = username
                if password:
                   cstr = '{u}:{p}'.format(u=cstr, p=password)
                cstr += '@{db}'.format(db=dbname)
            else:
                cstr = dbname
            LOG.debug('Create engine for database: '
                      'dbtype={}, dbname={}'.format(dbtype, dbname))
            engine = create_engine('{}://{}'.format(dbtype, cstr))
        except Exception as err:
            LOG.critical('Error: cannot start engine. {}'.format(err))
            raise err
        return engine

    @staticmethod
    def open_session(engine):
        session = None
        try:
            LOG.debug('Open session')
            session = sessionmaker(bind=engine)()
        except Exception as err:
            LOG.critical('Error: cannot open session. {}'.format(err))
            raise err
        return session

    @staticmethod
    def close_session(session):
        result = True
        try:
            LOG.debug('Close session')
            session.close_all()
        except Exception as e:
            LOG.error('Error: cannot close session. {}'.format(e))
            result = False
        return result

    @get_single_query_result
    def get_course_id_by_name(self, course_name):
        return self.session.query(DBClient.EduCourse.object_id).\
            filter(
            DBClient.EduCourse.object_id == DBClient.EduObject.object_id).\
            filter(DBClient.EduObject.object_name == course_name).\
            all()

    @get_single_query_result
    def get_status_id_by_name(self, status_name):
        return self.session.query(DBClient.EduObjectStatus.object_status_id).\
            filter(DBClient.EduObjectStatus.status_name == status_name).\
            all()

    @get_single_query_result
    def get_object_ref_by_id(self, object_id):
        return self.session.query(DBClient.EduObject.reference).\
            filter(DBClient.EduObject.object_id == object_id).\
            all()

    @get_first_query_result_if_any
    def get_student_id_by_phone_and_fio(self, phone, l_name='',
                                        f_name='', s_name=''):
        phone = re.sub(r'^\+7', '%', phone)
        phone = re.sub(r'^8', '%', phone)
        return self.session.query(DBClient.EduStudent.object_id).\
            filter(and_(or_(DBClient.EduStudent.home_phone.like(phone),
                            DBClient.EduStudent.mobile_phone.like(phone),
                            DBClient.EduStudent.work_phone.like(phone)),
                        or_(DBClient.EduStudent.last_name == l_name,
                            DBClient.EduStudent.first_name == f_name,
                            DBClient.EduStudent.second_name == s_name))).\
            all()

    @get_first_query_result_if_any
    def get_student_id_by_email_and_fio(self, email, l_name='',
                                        f_name='', s_name=''):
        return self.session.query(DBClient.EduStudent.object_id).\
            filter(and_(DBClient.EduStudent.e_mail == email,
                        or_(DBClient.EduStudent.last_name == l_name,
                            DBClient.EduStudent.first_name == f_name,
                            DBClient.EduStudent.second_name == s_name))).\
            all()

    @get_single_query_result
    def get_course_cost_by_id(self, course_id):
        return self.session.query(DBClient.EduCourse.course_cost).\
            filter(DBClient.EduCourse.object_id == course_id).\
            all()

    @get_single_query_result
    def get_course_duration_by_id(self, course_id):
        return self.session.query(DBClient.EduCourse.course_duration).\
            filter(DBClient.EduCourse.object_id == course_id).\
            all()

    def get_contract_number(self):
        cur_year = datetime.utcnow().strftime(u'%y')
        cnt_num_seq = randint(1, 10)
        contract_num = u'{n}/{y}'.\
                       format(n=cnt_num_seq,
                              y=cur_year)
        contract_num_as_dict = {'cnt_num': contract_num}
        return contract_num_as_dict['cnt_num']

    def _add_new_student(self, entry):
        student_id = None
        student_ref = None
        student_found = True
        if entry['mobile_phone']:
            LOG.debug(u'Get student ID by name and phone={}'.format(
                      str(entry['mobile_phone']).decode(DB_CODE)))
            student_id = self.get_student_id_by_phone_and_fio(
                    entry['mobile_phone'], entry['last_name'],
                    entry['first_name'], entry['second_name'])
        if not student_id:
            if entry['e_mail']:
                LOG.debug(u'Get student ID by name and email={}'.format(
                          str(entry['e_mail']).decode(DB_CODE)))
                student_id = self.get_student_id_by_email_and_fio(
                        entry['e_mail'], entry['last_name'],
                        entry['first_name'], entry['second_name'])
            if not student_id:
                student_found = False
                LOG.debug(u'Student not found. Add new student: '
                          u'phone={}, email={}'.format(
                          str(entry['mobile_phone']).decode(DB_CODE),
                          str(entry['e_mail']).decode(DB_CODE)))
                student_type_id = DBClient.EduObjectType['Student']
                student_status_id = \
                    self.get_status_id_by_name(entry['student_status'])
                new_student_object = DBClient.EduObject(
                        object_name=entry['full_name'],
                        object_type_id=student_type_id,
                        object_status_id=student_status_id
                )
                self.session.add(new_student_object)
                self.session.flush()
                student_id = new_student_object.object_id
                student_ref = self.get_object_ref_by_id(student_id)

                LOG.info(u'EduObject (added new record): id={id}, name={n}, '
                         u'type_id={t}, status_id={s}'.
                         format(
                             id=student_id,
                             n=str(entry['full_name']).decode(DB_CODE),
                             t=student_type_id, s=student_status_id
                         )
                )

                self.session.add(
                        DBClient.EduStudent(
                                object_id=student_id,
                                last_name=entry['last_name'],
                                first_name=entry['first_name'],
                                second_name=entry['second_name'],
                                mobile_phone=entry['mobile_phone'],
                                e_mail=entry['e_mail']
                        )
                )
                self.session.flush()

                LOG.info(u'EduStudent (added new record): '
                         u'id={id}, ref={ref}, '
                         u'l_name={l_n}, f_name={f_n}, s_name={s_n}, '
                         u'mobile={m}, e_mail={e}'.
                         format(
                             id=student_id, ref=student_ref,
                             l_n=str(entry['last_name']).decode(DB_CODE),
                             f_n=str(entry['first_name']).decode(DB_CODE),
                             s_n=str(entry['second_name']).decode(DB_CODE),
                             m=entry['mobile_phone'], e=entry['e_mail']
                         )
                )

        if student_id and not student_ref:
            student_ref = self.get_object_ref_by_id(student_id)

        if student_found:
            LOG.debug(u'Found student ID={}, ref={}'.format(
                    student_id, student_ref))

        return student_id, student_ref

    def _add_new_contract(self, entry, student_id, course_id):
        contract_type_id = DBClient.EduObjectType['Contract']
        contract_status_id = \
            self.get_status_id_by_name(entry['contract_status'])
        new_contract_object = DBClient.EduObject(
                object_type_id=contract_type_id,
                object_status_id=contract_status_id
        )
        self.session.add(new_contract_object)
        self.session.flush()
        contract_id = new_contract_object.object_id
        contract_ref = self.get_object_ref_by_id(contract_id)

        LOG.info(u'EduObject (added new record): id={id}, '
                 u'type_id={t}, status_id={s}'.
                 format(
                     id=contract_id,
                     t=contract_type_id, s=contract_status_id
                 )
        )

        course_cost = self.get_course_cost_by_id(course_id)
        course_duration = self.get_course_duration_by_id(course_id)
        LOG.debug(u'Found course by id {}.  Cost: {},  Duration: {}'.format(
                  course_id, course_cost, course_duration))
        cor_contract_num = self.get_contract_number()
        contract_num = str(cor_contract_num).decode(DB_CODE)
        LOG.debug(u'Generate new contract number: {}'.format(contract_num))
        nowtime = datetime.utcnow()
        hrs_per_day = 3
        timediff = timedelta(days=course_duration/hrs_per_day)
        new_contract = DBClient.EduContract(
            object_id=contract_id, student_id=student_id,
            course_id=course_id,
            begin_date=nowtime.date(),
            creation_date=nowtime,
            end_date=(nowtime + timediff).date(),
            contract_number=cor_contract_num,
            cost=course_cost
        )
        self.session.add(new_contract)
        self.session.flush()

        LOG.info(u'EduContract (added new record): id={id}, '
                 u'student_id={s_id}, course_id={c_id}, '
                 u'contract_num={num}, cost={cost}'.
                 format(
                     id=new_contract.object_id,
                     s_id=student_id, c_id=course_id,
                     num=contract_num,
                     cost=course_cost
                 )
        )

        return contract_id, contract_ref, contract_num

    def print_all_tables(self, filename=None):
        show_multi_data('Objects table:',
                        self.session.query(DBClient.EduObject).all(),
                        filename)
        show_multi_data('Object statuses table:',
                        self.session.query(DBClient.EduObjectStatus).all(),
                        filename)
        show_multi_data('Courses table:',
                        self.session.query(DBClient.EduCourse).all(),
                        filename)
        show_multi_data('Students table:',
                        self.session.query(DBClient.EduStudent).all(),
                        filename)
        show_multi_data('Contracts table:',
                        self.session.query(DBClient.EduContract).all(),
                        filename)


