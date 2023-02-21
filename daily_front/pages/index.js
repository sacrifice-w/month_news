import Head from 'next/head'
import Image from 'next/image'
import styles from '../styles/Home.module.css'
import Abstract from '../components/abstract'

export async function getStaticProps(){
  const res = await fetch('http://127.0.0.1:8000/posts')
  const posts = await res.json()
  return {
    props: {
      posts
    }
  }
}

export default function Home({posts}) {
  return (
    <div>
      <Abstract />

      <main className={styles.main}>
        <h1 className={styles.title}>
          <a href="https://www.cebnet.com.cn/">电子银行网</a>
        </h1>
        
        <ul className={styles.grid}>
          {posts.map((post) => (
            <a href={post.link} className={styles.card}>
              <h2>{post.title} &rarr;</h2>
                <p>来源：{' '}<code className={styles.code}>{post.source}</code></p>
            </a>
          ))}
        </ul>
      </main>

      <div className={styles.footer}>
        <a href="https://whcoding.cc" target="_blank">Powered by Wu</a>
      </div>
    </div>
  )
}
