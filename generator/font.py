import os

class Font:
    def __init__(self, path, cyr_small, cyr_capit, digits, chars=[], size_coef=1, y:int=0):
        self.path = path
        self.chars = chars
        self.size_coef = size_coef
        self.y = y # how many pixels we will add to default value

        if cyr_small:
            for char in range(1072, 1104):
                self.chars.append(chr(char))
            self.chars.append('ё')
        if cyr_capit:
            for char in range(1040, 1072):
                self.chars.append(chr(char))
        if digits:
            for i in range(0, 10):
                self.chars.append(str(i))

    def isValid(self, string):
        chars = set(string)
        for char in string:
            if char not in self.chars:
                return False
        return True

    def __str__(self):
        result = self.path + '\n'
        for char in self.chars:
            result += char + ' '
        return result

dirname = os.path.dirname(__file__)
DIR = os.path.join(dirname, 'content')
f = [Font(os.path.join(DIR,'Lemon Tuesday.otf'),True,True,False,list(' .,;:"()?'),0.8), \
Font(os.path.join(DIR,'ofont.ru_BetinaScriptCTT.ttf'),True,True,True,list(' +.,;:"-%$[]()«»!?/'),0.6), \
Font(os.path.join(DIR,'ofont.ru_Denistina.ttf'),True,True,True,list(' +.,;-:"()«/»!?'),0.8), \
Font(os.path.join(DIR,'ofont.ru_Eskal.ttf'),True,True,True,list(' +.,;-:"()/?!'),1), \
Font(os.path.join(DIR,'ofont.ru_Rozovii Chulok.ttf'),True,True,True,list(' +.,;-:"()«/»!?'),0.8), \
Font(os.path.join(DIR,'ofont.ru_Shlapak Script.otf'),True,True,True,list(' +.,;-:"()/!?'),1), \
Font(os.path.join(DIR,'werner4.ttf'),True,True,False,list(' +.,;:"()!?'),1), \
Font(os.path.join(DIR,'werner6.ttf'),True,True,False,list(' .,;:"()!?'),0.9), \
Font(os.path.join(DIR,'werner7.ttf'),True,True,False,list(' .,;:"()!?'),1), \
Font(os.path.join(DIR,'werner13.ttf'),True,True,False,list(' .,;:"()«»!'),1), \
Font(os.path.join(DIR,'werner14.ttf'),True,True,True,list(' %,./[]:;'),1), \
Font(os.path.join(DIR,'Jayadhira.ttf'),False,False,True,list(' +%,.-/()[]:;'),0.5), \
Font(os.path.join(DIR,'werner11.ttf'),True,True,False,list(' %,./[]:;'),1), \
Font(os.path.join(DIR,'werner15.ttf'),True,True,True,list(' +.,;:"()! '),1), \
Font(os.path.join(DIR,'werner16.ttf'),True,True,True,list(' +%,./()[]:;'),1), \
Font(os.path.join(DIR,'werner17.ttf'),True,True,False,list(' +%,./()[]:;'),1), \
Font(os.path.join(DIR,'bimbo.regular.ttf'),False,False,False,list(' +%,.-/()[]:;'),0.8), \
Font(os.path.join(DIR,'amandasignature.ttf'),False,False,True,list(' +%,.-/()[]:;'),0.5), \
Font(os.path.join(DIR,'mathilde.regular.otf'),False,False,True,list(' +%,.-/()[]:;'),0.5), \
Font(os.path.join(DIR,'werner2.ttf'),True,True,False,list('?!,.:;"()+[] '),1.4,-15), \
Font(os.path.join(DIR,'werner3.ttf'),True,True,False,list('?!,.:;"()+[] '),1.4,-10), \
Font(os.path.join(DIR,'werner5.ttf'),False,True,False,list('?!,.:;/-+[] '),1.4,-10), \
Font(os.path.join(DIR,'werner20.ttf'),True,False,True,list('%,./()[]:; '),1.4,-15), \
Font(os.path.join(DIR,'werner21.ttf'),True,False,True,list('%,./()[]:; '),1.4,-10), \
Font(os.path.join(DIR,'werner22.ttf'),True,False,True,list('"!%/,./()[]:; '),1.4,-15), \
Font(os.path.join(DIR,'werner23.ttf'),True,False,True,list('"!%/,./()[]:; '),1.4, -15), \
Font(os.path.join(DIR,'werner31.ttf'),True,False,True,list('"!%+,./"[]:; '),1.4,-15), \
Font(os.path.join(DIR,'werner36.ttf'),True,False,False,list('"!%+,./"()[]:; '),1.4,-15), \
Font(os.path.join(DIR,'werner37.ttf'),True,False,True,list('"!%+,./"()[]:; '),1.4,-15), \
Font(os.path.join(DIR,'werner10.ttf'),True,True,False,list(''),1.4, -10), \
Font(os.path.join(DIR,'werner30.ttf'),True,True,False,list(''),1.4, -10), \
Font(os.path.join(DIR,'werner39.ttf'),True,True,False,list(''),1.4, -10), \
Font(os.path.join(DIR,'werner40.ttf'),True,True,False,list(''),1.4, -10), \
Font(os.path.join(DIR,'werner41.ttf'),True,True,False,list(''),1.4, -10), \
Font(os.path.join(DIR,'werner42.ttf'),True,True,False,list(''),1.4, -10), \
Font(os.path.join(DIR,'werner43.ttf'),True,True,False,list(''),1.4, -10), \
Font(os.path.join(DIR,'ofont.ru_Marutya.ttf'),True,True,False,list(''),0.7, 10), \
Font(os.path.join(DIR,'GOST.TTF'),True,True,True,list('!@#$%^&*()_+-="%,./"[]:; '),0.5, 10), \
Font(os.path.join(DIR,'GOST_0.TTF'),True,True,True,list('!@#$%^&*()_+-="%,./"[]:; '),0.8, 10), \
Font(os.path.join(DIR,'gost_a.ttf'),True,True,True,list('!@#$%^&*()_+-="%,./"[]:; '),0.8, 10), \
Font(os.path.join(DIR,'GOST_AU.TTF'),True,True,True,list('!@#$%^&*()_+-="%,./"[]:; '),0.8, 10), \
Font(os.path.join(DIR,'gost_b.ttf'),True,True,True,list('!@#$%^&*()_+-="%,./"[]:; '),0.5, 15), \
Font(os.path.join(DIR,'GOST_BU.TTF'),True,True,True,list('!@#$%^&*()_+-="%,./"[]:; '),0.8,-5), \
Font(os.path.join(DIR,'gost_curve_b.ttf'),True,True,True,list('!@#$%^&*()_+-="%./"[]:; '), 0.55, 10), \
Font(os.path.join(DIR,'gost_curve.ttf'),True,True,True,list('!@#$%^&*()_+-="%,./"[]:; '),0.6,10), \
Font(os.path.join(DIR,'arial_bolditalicmt.ttf'),True,True,True,list('!@#$%^&*()_+-="%,./"[]:; '),0.6, 10), \
Font(os.path.join(DIR,'arialmt.ttf'),True,True,True,list('!@#$%^&*()_+-="%,./"[]:; '),0.7, 10), \
Font(os.path.join(DIR,'calibri.ttf'),True,True,True,list('!@#$%^&*()_+-="%,./"[]:; '),0.7, 10), \
Font(os.path.join(DIR,'calibri_bold.ttf'),True,True,True,list('!@#$%^&*()_+-="%,./"[]:; '),0.7,10), \
Font(os.path.join(DIR,'timesnewromanpsmt.ttf'),True,True,True,list('!@#$%^&*()_+-="%,./"[]:; '),0.7,10), \
Font(os.path.join(DIR,'cuyabra-Regular.ttf'),True,True,True,list('!@#$%^&*()_+-="%,./"[]:; '),0.55,10), \
Font(os.path.join(DIR,'ComicoroRu_0.ttf'),True,True,True,list('!@#$%^&*()_+-="%,./"[]:; '),0.8,10), \
Font(os.path.join(DIR,'Ostrovsky-Bold_0.otf'),True,True,True,list('!@#$%^&*()_+-="%,./"[]:; '),0.55,10), \
Font(os.path.join(DIR,'gogol_regular.otf'),True,True,True,list('!@#$%^&*()_+-="%,./"[]:; '),0.6,10), \
Font(os.path.join(DIR,'EBGaramond08-Regular.otf'),True,True,True,list('!@#$%^&*()_+-="%,./"[]:; '),0.8,10), \
Font(os.path.join(DIR,'EBGaramondSC08-Regular.otf'),True,True,True,list('!@#$%^&*()_+-="%,./"[]:; '),0.6,10), \
Font(os.path.join(DIR,'better-vcr-5.2.ttf'),True,True,True,list('!@#$%^&*()_+-="%,./"[]:; '),0.55,10), \
Font(os.path.join(DIR,'Madiffure-Demo.ttf'),True,True,True,list('!@#$%^&*()_+-="%,./"[]:; '),0.6,10), \
Font(os.path.join(DIR,'StampatelloFaceto.otf'),True,True,True,list('!@#$%^&*()_+-="%,./"[]:; '),0.6,10), \
Font(os.path.join(DIR,'the_weekend.otf'),True,True,True,list('!@#$%^&*()_+-="%,./"[]:; '),1,10), \
Font(os.path.join(DIR,'CruinnRegular.ttf'),True,True,True,list('!@#$%^&*()_+-="%,./"[]:; '),0.65,10), \
Font(os.path.join(DIR,'BartinaRegular.ttf'),True,True,True,list('!@#$%^&*()_+-="%,./"[]:; '),0.8,10), \
Font(os.path.join(DIR,'KelsonSansRU-Normal.otf'),True,True,True,list('!@#$%^&*()_+-="%,./"[]:; '),0.8,10)]