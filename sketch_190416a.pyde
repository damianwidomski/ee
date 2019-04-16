class Kwadrat():
    def __init__(self):
        pass
    def __init__(self,bok):
        self.bok=bok
    def sketch(self,x,y):
        self.x=x
        self.y=y
        rect(self.x,self.y,self.bok,self.bok)
class PasiastyKwadrat(Kwadrat):
    def sketchPasiasty(self,x,y,paski):
        Kwadrat.sketch(self,x,y)
        space=self.bok/paski
        xLinii=0
        for pasek in range(0,paski):
            line(x+xLinii,y,x+xLinii,y+self.bok)
            xLinii+=space
def setup():
    size(400,400)
    malyKwadrat = Kwadrat(50)
    malyKwadrat.sketch(200,300)
    duzyKwadrat=Kwadrat(200)
    duzyKwadrat.sketch(50,75)
    malyKwadrat.sketch(100,200)
    malyPasiastyKwadrat=PasiastyKwadrat(30.0)
    malyPasiastyKwadrat.sketchPasiasty(300,300,5)
    malyPasiastyKwadrat.sketchPasiasty(300,300,8)
