from pydantic import BaseModel


class Todo(BaseModel):
    title : str
    detail : str
    priority : str
    is_done : bool = False

    def __str__(self):
        output = f'name = {self.title}\n'
        output += f'priority = {self.priority}\n'
        output += f'detail = {self.detail}\n'
        if self.is_done:
            return output + 'status = Done'
        return output + 'status = Not Done'


# unused
'''priority_levels = {
    1 : 'Low',
    2 : 'Moderate',
    3 : 'High'
}'''
