package tacos;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

/**
 * @Description TODO
 * @Date 2022/5/26
 * @Created by 11599
 */
@Controller
public class MyController {

    @GetMapping("/home")
    public String home() {
        return "home";
    }
}
