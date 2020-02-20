import Control.Applicative
import Control.Monad
import System.IO
import Data.Char(isUpper)

wordCount = (1+) . length . (filter (==True)) . (map isUpper)

main :: IO ()
main = do
    s <- getLine
    putStrLn $ show $ wordCount s

getMultipleLines :: Int -> IO [String]

getMultipleLines n
    | n <= 0 = return []
    | otherwise = do          
        x <- getLine         
        xs <- getMultipleLines (n-1)    
        let ret = (x:xs)    
        return ret          

