import React, { memo } from "react";
import styled from 'styled-components';
import useSWR from 'swr';
import {
    ZoomableGroup,
    ComposableMap,
    Geographies,
    Geography
} from "react-simple-maps";


type ICovid = {
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

type Data = {
    data_world: ICovid,
    data_cases_continents: ICovid[],
    data_cases_countries: ICovid[]
}


const Container = styled.div`

width: 80%;
height: 600px;
display: flex;
overflow: hidden;

.worldmap-container {
    margin-left: auto;
    margin-right: auto;

    svg {
        height: 100%;
        margin-left: auto;
        margin-right: auto;
    }
}

`


const geoUrl =
    "https://raw.githubusercontent.com/zcreativelabs/react-simple-maps/master/topojson-maps/world-110m.json";


const rounded = (num: number) => {
    if (num > 1000000000) {
        return Math.round(num / 100000000) / 10 + "Bn";
    } else if (num > 1000000) {
        return Math.round(num / 100000) / 10 + "M";
    } else {
        return Math.round(num / 100) / 10 + "K";
    }
};

const WorldMap: React.FC<{ setTooltipContent: React.SetStateAction<any> }> = ({ setTooltipContent }) => {

    const fetcher = (url: string) => fetch(url)
        .then(res => res.json());

    const { data, error } = useSWR<Data>('http://127.0.0.1:8000/covidmap/get-todays-data/?format=json', fetcher);

    return (
        <>
            {error && !data && <div className="failed-data">Failed. </div>}

            {!data && !error && <div className='loading-window'>Loading...</div>}

            {
                <Container>
                    <div className="worldmap-container">
                        <ComposableMap data-tip="" projectionConfig={{ scale: 200 }} height={600} width={1100}>
                            <Geographies geography={geoUrl}>
                                {({ geographies }) =>
                                    geographies.map(geo => (
                                        <Geography
                                            key={geo.rsmKey}
                                            geography={geo}
                                            onMouseEnter={() => {
                                                const { NAME, NAME_LONG, POP_EST } = geo.properties;

                                                let newCases: number;
                                                let newDeaths: number;
                                                let newTests: number;
                                                let newVaccinations: number;
                                                let totalCases: number;
                                                let totalDeaths: number;
                                                let peopleVaccinated: number;
                                                let populationDensity: number;

                                                data.data_cases_countries.forEach((country) => {
                                                    if (country.location_name === NAME || country.location_name == NAME_LONG) {
                                                        newCases = country.new_cases_smoothed;
                                                        newDeaths = country.new_deaths_smoothed;
                                                        newTests = country.new_tests_smoothed;
                                                        newVaccinations = country.new_vaccinations_smoothed;
                                                        totalCases = country.total_cases;
                                                        totalDeaths = country.total_deaths;
                                                        peopleVaccinated = country.people_vaccinated;
                                                        populationDensity = country.population_density;

                                                        
                                                        return;
                                                    }
                                                })

                                                setTooltipContent(`${NAME} — ${rounded(POP_EST)}
                                                New Cases: ${newCases? rounded(newCases): "unknown"},
                                                New Deaths: ${newDeaths? rounded(newDeaths): "unknown"},
                                                New Tests: ${newTests? rounded(newTests): "unknown"},
                                                New Vaccinations: ${newVaccinations? rounded(newVaccinations): "unknown"},
                                                Total Cases: ${totalCases? rounded(totalDeaths): "unknown"},
                                                Total Deaths: ${totalDeaths? rounded(totalDeaths): "unkown"}
                                                People Vaccinated: ${peopleVaccinated? rounded(peopleVaccinated): "unknown"}
                                                Population Density: ${populationDensity? rounded(populationDensity): "unknown"}`);
                                            }}
                                            onMouseLeave={() => {
                                                setTooltipContent("");
                                            }}
                                            style={{
                                                default: {
                                                    fill: "#D6D6DA",
                                                    outline: "none"
                                                },
                                                hover: {
                                                    fill: "#F53",
                                                    outline: "none"
                                                },
                                                pressed: {
                                                    fill: "#E42",
                                                    outline: "none"
                                                }
                                            }}
                                        />
                                    ))
                                }
                            </Geographies>
                        </ComposableMap>
                    </div>


                    {/* {JSON.stringify(data)} */}
                </Container>
            }

        </>
    );
};

export default memo(WorldMap);
