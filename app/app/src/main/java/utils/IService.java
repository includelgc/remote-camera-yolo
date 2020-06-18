package utils;

import okhttp3.ResponseBody;
import retrofit2.Call;
import retrofit2.http.GET;
import retrofit2.http.Streaming;


public interface IService {
    String BASE_URL = "http://47.110.146.191:5000/";
    String PATH = "download";

    @GET(PATH)
    Call<ResponseBody> getPicture();
}
