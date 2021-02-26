import useSWR from 'swr';
import { AppProps } from 'next/app';
import Image from 'next/image';
import Head from 'next/head';
import '../styles/global.css';

type ICovid = {
    continent: string,
    location: string,
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




const fetcher = (url: string) => fetch(url)
    .then(res => res.json())
    .catch(err => console.log(err));


function App({ Component, pageProps }: AppProps) {

    const { data, error } = useSWR<Data>('http://127.0.0.1:8000/covidmap/get-todays-data/?format=json', fetcher);


    return (
        <div>
            <Head>
                <title>Covid World Map</title>
                <link rel="preconnect" href="https://fonts.gstatic.com" />
                <link href="https://fonts.googleapis.com/css2?family=Barlow:wght@300;400;500&display=swap" rel="stylesheet" />
            </Head>


            <body>
                <nav>
                    <h1>Covid World Map
                        <span className="nav-image">
                            <Image
                                src="/nav/world.svg"
                                alt="world"
                                width={28}
                                height={28}
                            />
                        </span>

                    </h1>
                </nav>

                {
                    error ? <div>Failed {JSON.stringify(error)}</div>
                        :
                        !data ? <div className='loading-window'>Loading...</div>
                            :
                            <div>
                                {JSON.stringify(data)}
                            </div>
                }


            </body>
        </div>
    )


}

export default App;