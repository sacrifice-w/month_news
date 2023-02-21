import Head from 'next/head'
import styles from '../styles/Home.module.css'

export default function Abstract( ) {
    return(
        <div>
            <Head>
                <title>每日新闻</title>
                <meta name="description" />
                <link rel="icon" href="/favicon.png" />
            </Head>

            <div className={styles.head}>
                <a href="" className={styles.headBlock}><p>每日新闻</p></a>
                <a href="" className={styles.headBlock}><p>政策发布</p></a>
                <a href="" className={styles.headBlock}><p>公众号消息</p></a>
            </div>
        </div>
    )
}