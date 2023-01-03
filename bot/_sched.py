import zoneinfo

from apscheduler.executors.asyncio import AsyncIOExecutor
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.schedulers.asyncio import AsyncIOScheduler


def get_scheduler():
    jobstores = {"default": SQLAlchemyJobStore(url="sqlite:///jobs.sqlite")}
    executors = {"default": AsyncIOExecutor()}
    scheduler = AsyncIOScheduler(jobstores=jobstores, executors=executors, timezone=zoneinfo.ZoneInfo("UTC"))
    return scheduler
