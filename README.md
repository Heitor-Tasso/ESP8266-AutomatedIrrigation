# ESP8266-AutomatedIrrigation

<!---Esses são exemplos. Veja https://shields.io para outras pessoas ou para personalizar este conjunto de escudos. Você pode querer incluir dependências, status do projeto e informações de licença aqui--->

![GitHub repo size](https://img.shields.io/github/repo-size/Heitor-Tasso/ESP8266-AutomatedIrrigation?style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/Heitor-Tasso/ESP8266-AutomatedIrrigation?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/Heitor-Tasso/ESP8266-AutomatedIrrigation?style=for-the-badge)
![Bitbucket open issues](https://img.shields.io/bitbucket/issues/Heitor-Tasso/ESP8266-AutomatedIrrigation?style=for-the-badge)
![Bitbucket open pull requests](https://img.shields.io/bitbucket/pr-raw/Heitor-Tasso/ESP8266-AutomatedIrrigation?style=for-the-badge)

<img src="exemplo-image.png" alt="Imagem de Exemplo">

> Utilizamos o ESP8266 para automatizar os cuidados de uma planta, sendo possível visualizar a saúde. Assim, facilitando os cuidados e consequêntemente aumentando a venda de plantas domésticas. 

### Ajustes e melhorias

O projeto ainda está em desenvolvimento e as próximas atualizações serão voltadas nas seguintes tarefas:

- [ ] Opção de poder utlizar o Wifi residencial
- [ ] Visualização pela plataforma
- [ ] Média de saúde de cada planta
- [x] Configurar WiFi pelo celular

## 💻 Pré-requisitos

Antes de começar, verifique se você atendeu aos seguintes requisitos:
<!---Estes são apenas requisitos de exemplo. Adicionar, duplicar ou remover conforme necessário--->
* Você instalou o `Python >= 3.9.7`.
* Você tem uma máquina `Windows / Linux / Mac / Android`.

## 🚀 Instalando o ESP8266-AutomatedIrrigation

Para instalar o ESP8266-AutomatedIrrigation, siga estas etapas:

Instruções:

 - Abrir o aquivo Arduino/Arduino.ino na IDE do Arduino.
 - Configurar para poder utlizar o ESP8266 [esp8266 no arduino ide](https://www.robocore.net/tutoriais/programando-o-esp8266-pela-arduino-ide).
 - Instalar o driver do ESP8266 [como instalar o driver](https://www.blogdarobotica.com/2020/05/26/instalando-driver-serial-para-nodemcu-com-chip-ch340/#:~:text=Caso%20a%20placa%20NODEMCU%20ESP8266,NODEMCU%20ESP8266%20n%C3%A3o%20foi%20reconhecida.&text=Ap%C3%B3s%20a%20conclus%C3%A3o%20do%20download,instala%C3%A7%C3%A3o%2C%20conforme%20a%20Figura%205.).
  - Carregar site no ESP8266 [como carregar arquivos no esp8266](https://randomnerdtutorials.com/install-esp8266-filesystem-uploader-arduino-ide/).
  - Carregar o programa no ESP8266 [como colocar o programa no esp8266](https://seurobo.com.br/como-enviar-o-programa-para-o-arduino-uno-mega-ou-outros/).
  - Compilar o App MorePlant para a sua máquina [compilar apps com Kivy](https://kivy.org/doc/stable/guide/packaging.html) ou instalar utilizando os links mais abaixo.
  - Agora é só ligar o ESP8266 e entrar no App para se conectar.

Downloads MorePlant:
 - `Windows` -> [Download MorePlant]()
 - `Mac` -> [Download MorePlant]()
 - `Android` -> [Download MorePlant]()

## ☕ Utilizando o ESP8266-AutomatedIrrigation

Para usar o MorePlant, siga estas etapas:

 - Conecte-se à rede Wifi que o ESP8266 está conectado.
 - Inicialize o App e logue com sua conta.
 - Leia o QRCode do ESP8266 e tira e configure a Planta utilizada.
 - Agora é só apertar em iniciar e deixar que sua planta seja monitorada.


## 📫 Contribuindo para o ESP8266-AutomatedIrrigation
<!---Se o seu README for longo ou se você tiver algum processo ou etapas específicas que deseja que os contribuidores sigam, considere a criação de um arquivo CONTRIBUTING.md separado--->
Para contribuir com o ESP8266-AutomatedIrrigation, siga estas etapas:

1. Bifurque este repositório.
2. Crie um branch: `git checkout -b dev`.
3. Faça suas alterações e confirme-as: `git commit -m '<mensagem_commit>'`
4. Envie para o branch: `git push origin dev`
5. Crie a solicitação de pull.

Como alternativa, consulte a documentação do GitHub em [como criar uma solicitação pull](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).

## 🤝 Colaboradores

Agradecemos às seguintes pessoas que contribuíram para este projeto:

<table>
  <tr>
    <td align="center">
      <a href="#">
        <img src="https://avatars.githubusercontent.com/u/87236158?v=4" width="100px;" alt="Foto do Heitor-Tasso no GitHub"/><br>
        <sub>
          <b>Heitor Tasso</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="#">
        <img src="https://s2.glbimg.com/FUcw2usZfSTL6yCCGj3L3v3SpJ8=/smart/e.glbimg.com/og/ed/f/original/2019/04/25/zuckerberg_podcast.jpg" width="100px;" alt="Foto do Mark Zuckerberg"/><br>
        <sub>
          <b>Mark Zuckerberg</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="#">
        <img src="https://miro.medium.com/max/360/0*1SkS3mSorArvY9kS.jpg" width="100px;" alt="Foto do Steve Jobs"/><br>
        <sub>
          <b>Steve Jobs</b>
        </sub>
      </a>
    </td>
  </tr>
</table>


## 📝 Licença

Esse projeto está sob licença. Veja o arquivo [LICENÇA](LICENSE.md) para mais detalhes.

[⬆ Voltar ao topo](#ESP8266-AutomatedIrrigation)<br>
# ESP8266-AutomatedIrrigation

Ver quantidade de linhas do código:
 - `(gci -include *.kv,*.py,*.ino,*.cpp,*.h,*.html,*.css -recurse | select-string .).Count`
