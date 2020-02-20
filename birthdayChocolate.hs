import Control.Applicative
import Control.Monad
import System.IO

getNSubdivs m d squares
    | length squares >= m = n + (getNSubdivs m d $ tail squares)
    | otherwise = 0
    where
        n = if d == (sum $ take m squares) then 1 else 0


main :: IO ()
main = do
    n_temp <- getLine
    let n = read n_temp :: Int
    s_temp <- getLine
    let s = map read $ words s_temp :: [Int]
    d_temp <- getLine
    let d_t = words d_temp
    let d = read $ d_t!!0 :: Int
    let m = read $ d_t!!1 :: Int
    putStrLn $ show $ getNSubdivs m d s

getMultipleLines :: Int -> IO [String]

getMultipleLines n
    | n <= 0 = return []
    | otherwise = do          
        x <- getLine         
        xs <- getMultipleLines (n-1)    
        let ret = (x:xs)    
        return ret  