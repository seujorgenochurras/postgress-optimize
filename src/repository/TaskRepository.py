from src.injector import Injector
from src.repository.AbstractRepository import AbstractRepository
from prisma.types import TaskCreateInput
from prisma.enums import TaskStatus
from prisma.partials import SimpleTask
from prisma.models import User

@Injector(alias=AbstractRepository)
class TaskRepository(AbstractRepository):
    async def create(self, task: TaskCreateInput):
        return await self._db.task.create(data=task)

    async def find_status_by_user(self, user_id: int, status: TaskStatus):
        return await SimpleTask.prisma().find_many(
            where={
                "card": {"is": {"active": True, "user": {"is": {"id": user_id}}}},
                "status": status,
            },
        )

    async def find_status_by_user_slow(self, user_id : int, status : TaskStatus):
        return await User.prisma().find_first(
            where={"id" : user_id},
            include={
            "cards": {
                "where": {
                    "userId" : user_id,
                    "active": True,
                },
                 "include": {
                     "tasks": {
                         "where": {
                             "status": status
                         }
                     }
                     
                 }
                
            },
            
        })