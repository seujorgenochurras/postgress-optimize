import random
from locust import HttpUser, task, between


class UserBehavior(HttpUser):
    wait_time = between(1, 5)  # Wait time between tasks in seconds

    @task
    def get_user_task(self):
        random_user_id = random.randint(1, 10000)
        self.client.get(
            f"/api/user/{random_user_id}/task", headers={"accept": "application/json"}
        )
