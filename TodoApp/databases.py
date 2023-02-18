import sqlite3


class DB():
    def __init__(self) -> None:
        super().__init__()
        self.createTaskDatabase()
        
    
    def createTaskDatabase(self):
        self.__db = sqlite3.connect("tasks.sqlite", check_same_thread=False)
        
        with self.__db:

            self.__cursor =  self.__db.cursor()

            self.__cursor.execute('''CREATE TABLE IF NOT EXISTS yapilacaklar
                (content_id INTEGER PRIMARY KEY,
                    title NOT NULL,
                    content NOT NULL
                   
                    )'''
                )
            

    def addData(self, title:str, content: str):
        
        self.__cursor.executemany('INSERT INTO yapilacaklar(title, content) VALUES (?,?)', [(title, content)])
        self.__db.commit()
            
    
    def getTotalContent(self):
        data = self.__cursor.execute("SELECT * From yapilacaklar").fetchall()
        return data[::-1]
    
    def delete(self, idTask:int):
        self.__cursor.execute("DELETE FROM yapilacaklar WHERE content_id = ?",(idTask,))
        print("silindi")
        self.__db.commit()
            

    def queryIdNumber(self, Id:int):
        __IdNumber = self.__cursor.execute("SELECT * From yapilacaklar WHERE content_id = ?", (int(Id),)).fetchone()
        if __IdNumber != None:
            return (__IdNumber)
        
        else:
            return False
        
    def update(self, id:int, title:str, content:str):
        self.__cursor.execute("UPDATE yapilacaklar SET title = ?, content = ? WHERE content_id = ?",(title, content, id))
        self.__db.commit()
        print("güncellendi")
        
