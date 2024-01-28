class Chain:

    def __init__(self, argo):
        if isinstance(argo, int) or isinstance(argo, str):
            self.argo = argo
        else:
            raise Exception

    def __call__(self, new_argo):
        assert type(self.argo) == type(new_argo), "invalid operation"
        if isinstance(new_argo, int):
            self.argo += new_argo
            return Chain(self.argo)
        elif isinstance(new_argo, str):
            self.argo = self.argo + " " + new_argo
            return Chain(self.argo)
        else:
            raise Exception(" invalid operation")

    def __str__(self):
        return f"{self.argo}"


print(Chain("alo"))
