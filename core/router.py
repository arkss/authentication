class MyRouter:
    """
    user_data 앱의 모델에서 수행되는 모든 데이터베이스 연산을 제어하는 중계기
    """
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'salt':
            return 'salt_db'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'salt':
            return 'salt_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'salt' or \
           obj2._meta.app_label == 'salt':
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'salt':
            return db == 'salt_db'
        return None