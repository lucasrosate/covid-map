export default interface ICovid {
    continent_name: string,
    location_name: string,
    date_registered: string,
    new_cases_smoothed: number,
    new_deaths_smoothed: number,
    new_tests_smoothed: number,
    new_vaccinations_smoothed: number,
    total_cases: number,
    total_deaths: number,
    people_vaccinated: number,
    population_density: number,
    population: number,
    life_expectancy: number,
    human_development_index: number
}