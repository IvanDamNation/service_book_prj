import React from "react";
import "../styles/App.scss";
import MAIN_LOGO from './public/img/logo_main.svg';
import LOGO_MINI1 from './public/img/Logotype_accent RGB_1.png';
import LOGO_MINI2 from './public/img/Logotype_accent RGB_2.png';
import LOGO_MINI3 from './public/img/Logotype_accent RGB_3.png';



export const App = () => {
	return (
    <div className="wrapper">
      <header>
        <div className="headerContainer">
          <ul className="headerUp">
            <li className="logo">
              <img
                src={MAIN_LOGO}
                alt="logo_silant"
                width="400"
              />
            </li>
            <li className="contactTelephone">
              <h3>+7-8352-20-12-09, telegram</h3>
            </li>
            <li className="authButton">
              <button type="submit">Авторизация</button>
            </li>
          </ul>
          <div className="headerDown">
            <h1>Электронная сервисная книжка "Мой Силант"</h1>
          </div>
        </div>
      </header>
      <main>
        <div className="content" hidden>
          <p className="mainInfo">
            Проверьте комплектацию и технические характеристики
            техники Силант
          </p>
          <form className="searchMachine" action="!#" method="post">
            <div className="searchText">
              Поиск по заводскому номеру:
            </div>
            <input className="searchInput" type="text" placeholder="Введите номер..." />
            <button className="searchButton" type="submit">Поиск</button>
          </form>
          <p className="searchResult">Результат поиска:</p>
          <div className="searchInfo">
            <h2 className="searchInfoHead">Информация о комплектации и технических характеристиках Вашей техники</h2>
            <div className="tableContainer">
              <table className="searchInfoTable">
                <thead>
                  <tr>
                    <th>One</th>
                    <th>Two</th>
                    <th>Three</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td data-label="One">Four</td>
                    <td data-label="Two">Five</td>
                    <td data-label="Three">Six</td>
                  </tr>
                  <tr>
                    <td data-label="One">Seven</td>
                    <td data-label="Two">Eight</td>
                    <td data-label="Three">Nine</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
        <div className="contentAuth">
          <div className="contentAuthMainInfo" hidden>
            <p className="mainInfo">
              Основная панель
            </p>
            <div className="headerDown">
              <h2>Клиент/Сервисная компания (от кого авторизовались)</h2>
            </div>
            <div className="searchInfo">
              <div className="searchInfoHeadContainer"></div>
              <h2 className="searchInfoHead">Информация о комплектации и технических характеристиках Вашей техники</h2>
              <div className="infoNavContainer">
                  <ul className="infoNav">
                    <li>
                      <button className="mainInfoBtn">Общая инфо</button>
                    </li>
                    <li>
                      <button className="mainInfoBtn">Техобслуживание</button>
                    </li>
                    <li>
                      <button className="mainInfoBtn">Рекламации</button>
                    </li>
                  </ul>
                </div>
              <div className="tableContainer">
                <table className="searchInfoTable">
                  <thead>
                    <tr>
                      <th>One</th>
                      <th>Two</th>
                      <th>Three</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td data-label="One">Four</td>
                      <td data-label="Two">Five</td>
                      <td data-label="Three">Six</td>
                    </tr>
                    <tr>
                      <td data-label="One">Seven</td>
                      <td data-label="Two">Eight</td>
                      <td data-label="Three">Nine</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </div>
        <div className="contentAuthTechnical">
          <p className="mainInfo">
            Основная панель
          </p>
          <div className="headerTechnical">
            <h3 className="headerTechnicalInfo">Машина 1</h3>
            <h4 className="headerTechnicalInfo">Заводской номер</h4>
          </div>
          <div className="searchInfo">
            <div className="searchInfoHeadContainer"></div>
            <h2 className="searchInfoHead">Информация о проведении технического обслуживания Вашей техники</h2>
            <div className="infoNavContainer">
                <ul className="infoNav">
                  <li>
                    <button className="mainInfoBtn">Общая инфо</button>
                  </li>
                  <li>
                    <button className="mainInfoBtn">Техобслуживание</button>
                  </li>
                  <li>
                    <button className="mainInfoBtn">Рекламации</button>
                  </li>
                </ul>
              </div>
            <div className="tableContainer">
              <table className="searchInfoTable">
                <thead>
                  <tr>
                    <th>One</th>
                    <th>Two</th>
                    <th>Three</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td data-label="One">Four</td>
                    <td data-label="Two">Five</td>
                    <td data-label="Three">Six</td>
                  </tr>
                  <tr>
                    <td data-label="One">Seven</td>
                    <td data-label="Two">Eight</td>
                    <td data-label="Three">Nine</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
      <div className="descriptionContainer">
        <div className="description">
          Описание Lorem ipsum dolor sit amet consectetur adipisicing elit. Debitis magni fugiat veniam maiores officia, laudantium hic? Velit nobis soluta animi eum dolorem libero sapiente sed aliquid? Architecto consequatur provident quae!
        </div>
      </div>
      </main>
      <footer>
        <div className="footer">
          <ul className="footerContainer">
            <li className="contactTelephoneFooter">
              <h3>+7-8352-20-12-09, telegram</h3>
            </li>
            <li>
              <img src={LOGO_MINI1} width={100} alt="Logo_mini1" />
            </li>
            <li>
            <img src={LOGO_MINI2} width={100} alt="Logo_mini2" />
            </li>
            <li>
            <img src={LOGO_MINI3} width={100} alt="Logo_mini3" />
            </li>
            <li className="footInfo">
              Мой Силант 2022
            </li>
          </ul>
        </div>
      </footer>
    </div>
  );
}