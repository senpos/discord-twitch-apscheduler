import zoneinfo
from functools import lru_cache

from apscheduler.executors.asyncio import AsyncIOExecutor
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.schedulers.asyncio import AsyncIOScheduler


@lru_cache(maxsize=1)
def get_scheduler():
    jobstores = {"default": SQLAlchemyJobStore(url="sqlite:///jobs.sqlite")}
    executors = {"default": AsyncIOExecutor()}
    scheduler = AsyncIOScheduler(jobstores=jobstores, executors=executors, timezone=zoneinfo.ZoneInfo("UTC"))
    return scheduler
