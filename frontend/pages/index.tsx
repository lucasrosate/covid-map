  import App, { AppProps } from 'next/app';

  


export default function Index({ Component, pageProps } : AppProps) {
  return <Component {...pageProps} />
}
