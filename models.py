from sqlalchemy import Column, Integer, String, Time, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


engine = create_engine("sqlite:///database.sqlite3", echo=True)
Base = declarative_base()


class Schedule(Base):
    __tablename__ = 'schedule'

    id = Column(Integer, primary_key=True)
    day_week = Column(String(20), nullable=False)
    name_couple = Column(String(50), nullable=False)
    description_couple = Column(String(250), nullable=True)
    time_start_couple = Column(Time, nullable=False)
    time_end_couple = Column(Time, nullable=False)
    teacher_couple = Column(String(50), nullable=False)
    audience_couple = Column(String(50), nullable=False)
    type_week = Column(String(100), nullable=False)

    def start_couple(self):
        return f"Зараз {self.name_couple}.\n" \
               f"Викладач: {self.teacher_couple}\n" \
               f"Аудиторія: {self.audience_couple}\n" \
               f"Опис: {self.description_couple}\n" \
               f"Час початку: {self.time_start_couple}\n" \
               f"Час закінчення: {self.time_end_couple}\n" \
               f"Тиждень: {self.type_week}\n" \
               f"День тижня: {self.day_week}"

    def end_couple(self):
        return f"Пара {self.name_couple} закінчилась.\n" \
               f"Викладач: {self.teacher_couple}\n" \
               f"Аудиторія: {self.audience_couple}\n" \
               f"Опис: {self.description_couple}\n" \
               f"Час початку: {self.time_start_couple}\n" \
               f"Час закінчення: {self.time_end_couple}\n" \
               f"Тиждень: {self.type_week}\n" \
               f"День тижня: {self.day_week}"

    def __repr__(self):
        return f"<Schedule(" \
               f"id={self.id!r}, " \
               f"name_couple={self.name_couple!r}, " \
               f"description_couple={self.description_couple!r}, " \
               f"time_start_couple={self.time_start_couple!r}, " \
               f"time_end_couple={self.time_end_couple!r}, " \
               f"teacher_couple={self.teacher_couple!r}, " \
               f"audience_couple={self.audience_couple!r}" \
               f")>"


Base.metadata.create_all(engine)
session = sessionmaker(bind=engine)()
