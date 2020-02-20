import Control.Applicative
import Control.Monad
import System.IO

firstCat x y z
    | d1 < d2 = "Cat A"
    | d1 > d2 = "Cat B"
    | otherwise = "Mouse C"
    where
        d1 = abs $ z-x
        d2 = abs $ z-y

main :: IO ()
main = do
    q_temp <- getLine
    let q = read q_temp :: Int
    forM_ [1..q] $ \a0  -> do
        x_temp <- getLine
        let x_t = words x_temp
        let x = read $ x_t!!0 :: Int
        let y = read $ x_t!!1 :: Int
        let z = read $ x_t!!2 :: Int
        putStrLn $ firstCat x y z

getMultipleLines :: Int -> IO [String]

getMultipleLines n
    | n <= 0 = return []
    | otherwise = do          
        x <- getLine         
        xs <- getMultipleLines (n-1)    
        let ret = (x:xs)    
        return ret          

