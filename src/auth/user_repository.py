class UserRepository:
    def __init__(self):
        pass

    async def referrer_check(self, ref_tid: int, new_user_tid: int) -> bool:
        print(ref_tid, new_user_tid)
        return  True