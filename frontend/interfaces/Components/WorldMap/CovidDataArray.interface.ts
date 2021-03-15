import ICovid from './ICovid.interface';

type CovidDataArray = {
    data_world: ICovid,
    data_cases_continents: ICovid[],
    data_cases_countries: ICovid[]
}

export default CovidDataArray;