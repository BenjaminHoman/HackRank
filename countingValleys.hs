import Control.Applicative
import Control.Monad
import System.IO

withElevation s = map (\x -> (x, 0)) s

calcElevation s = tail $ scanl fn ('N', 0) s
    where 
        fn (dir1, e1) (dir2, e2)
            | dir2 == 'U' = (dir2, e1+1)
            | dir2 == 'D' = (dir2, e1-1)
            | otherwise = (dir2, e1)

valleyCount s = sum $ map fn $ (calcElevation . withElevation) s
    where fn (dir, e) = if dir=='U' && e==0 then 1 else 0

main :: IO ()
main = do
    n_temp <- getLine
    let n = read n_temp :: Int
    s <- getLine
    putStrLn $ show $ valleyCount s

getMultipleLines :: Int -> IO [String]

getMultipleLines n
    | n <= 0 = return []
    | otherwise = do          
        x <- getLine         
        xs <- getMultipleLines (n-1)    
        let ret = (x:xs)    
        return ret          

