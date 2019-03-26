class AuditManager:
    def add_call(self, *args, **kwargs):
        pass
    def add_result(self, *args, **kwargs):
        pass

audit_service = AuditManager()

class CmdManager:
    def set_service(self, service):
        self.service = service
        self.service.start()

    def run_command(self, cmd):
        audit_service.add_call(self.service.name, 'run', cmd)
        result = self.service.run(cmd)
        audit_service.add_result(self.service.name, 'run', result)
