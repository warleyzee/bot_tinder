from selenium import webdriver
from time import sleep


class TinderBot:
    def __init__(self, ):
        self.driver = webdriver.Chrome(executable_path='chromedriver.exe')
        self.driver.get('https://www.tinder.com')
        sleep(3)

    def login(self, ):
        botao_login = self.driver.find_element_by_xpath('//*[@id="s1502865376"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
        sleep(3)
        botao_login.click() 
        sleep(3)

    def logar_com_telefone(self, ):
        logar_com_telefone = self.driver.find_element_by_xpath('//*[@id="s-225515700"]/div/div/div[1]/div/div[3]/span/div[3]/button')
        sleep(3)
        logar_com_telefone.click()
        sleep(3)

    def esperar_input_manual(self, ):
        input()

    def fechar_notificacao_de_localizacao(self,):
        permiti_localizacao = self.driver.find_element_by_xpath('//*[@id="s-225515700"]/div/div/div/div/div[3]/button[1]')
        sleep(3)
        permiti_localizacao.click() 
        sleep(3)

    def fechar_pop_up_notificacoes(self,):
        pop_up_notificacao =  self.driver.find_element_by_xpath('//*[@id="s-225515700"]/div/div/div/div/div[3]/button[2]') 
        sleep(3)
        pop_up_notificacao.click() 
        sleep(3)

    def dar_like(self,):
        try:
            sleep(3)
            botao_curtir = self.driver.find_elements_by_xpath('//div[@class="Mx(a) Fxs(0) Sq(70px) Sq(60px)--s"]//button')[1]
        except:
            try:
                sleep(3)
                botao_curtir = self.driver.find_elements_by_xpath('//div[@class="Mx(a) Fxs(0) Sq(70px) Sq(60px)--s Bd Bdrs(50%) Bdc($c-like-green)"]//button')  
                sleep(3)
                botao_curtir.click()
                sleep(3) 
            except:
                pass
        finally:
            sleep(3)
            botao_curtir.click()
            try:
                if self.driver.find_element_by_xpath("//label[text()='Say something nice!']") is not None:
                    fechar_janela_match = self.driver.find_element_by_xpath("//button[@title='Back to Tinder']")
                    fechar_janela_match.click()
            except:
                pass


bot = TinderBot()
bot.login()
bot.logar_com_telefone()
bot.esperar_input_manual()
bot.fechar_notificacao_de_localizacao()
bot.fechar_pop_up_notificacoes()

while True:
    bot.dar_like()