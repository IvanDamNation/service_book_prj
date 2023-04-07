import React from "react";


const SearchByNumber = () => {
    return (
        <form className="searchMachine" action="!#" method="post">
            <div className="searchText">Поиск по заводскому номеру:</div>
            <input
                className="searchInput"
                type="text"
                placeholder="Введите номер..."
            />
            <button className="searchButton" type="submit">
                Поиск
            </button>
        </form>
    );
}

export default SearchByNumber;