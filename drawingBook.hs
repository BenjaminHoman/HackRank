import Control.Applicative
import Control.Monad
import System.IO

minFlips total page = min fromStart fromEnd
    where
        fromStart = abs $ (toFace 0) - (toFace page)
        fromEnd = abs $ (toFace total) - (toFace page)
        toFace p = p `div` 2

main :: IO ()
main = do
    n_temp <- getLine
    let n = read n_temp :: Int
    p_temp <- getLine
    let p = read p_temp :: Int
    putStrLn $ show $ minFlips n p

getMultipleLines :: Int -> IO [String]

getMultipleLines n
    | n <= 0 = return []
    | otherwise = do          
        x <- getLine         
        xs <- getMultipleLines (n-1)    
        let ret = (x:xs)    
        return ret          

