from typing import Optional

class Settings:
  db_username: Optional[str] = None
  db_password: Optional[str] = None
  db_name: Optional[str] = None
  db_port: Optional[str] = None

  @property
  def db_url(self):
    #return f'postgresql://{self.db_username}:{self.db_password}@db:{self.db_port}/{self.db_name}'
    return 'sqlite:////home/matheus/Downloads/mini_ecommerce_clean/database.db'

settings = Settings()