import React from "react";
import "../styles/App.scss";
import MAIN_LOGO from './public/img/logo_main.svg';


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
        <div className="content">
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
      </main>
      <footer className="none">
        <div className="footer">
          <ul className="footerContainer">
            <li className="contactTelephoneFooter">
              <h3>+7-8352-20-12-09, telegram</h3>
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